"""Utility tools that can be invoked by the I.A. agent."""

from __future__ import annotations

import ast
import json
import operator
import re
from dataclasses import dataclass
from difflib import get_close_matches
from pathlib import Path
from typing import Iterable, Protocol

from .memory import Memory

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


class Tool(Protocol):
    """Tool interface for extending the agent."""

    name: str
    description: str

    def can_handle(self, query: str) -> bool:
        ...

    def run(self, query: str, memory: Memory) -> str:
        ...


@dataclass
class MathTool:
    """Evaluate safe mathematical expressions."""

    name: str = "math"
    description: str = "Resolve cálculos matemáticos simples com segurança."
    expression_pattern: re.Pattern[str] = re.compile(r"([0-9][0-9\s\+\-\*\/\(\)\.%\^]*)")

    def can_handle(self, query: str) -> bool:
        return self._extract_expression(query) is not None

    def run(self, query: str, memory: Memory) -> str:
        expression = self._extract_expression(query)
        if expression is None:
            return "Não reconheci uma expressão matemática para resolver."
        try:
            tree = ast.parse(expression, mode="eval")
            result = self._eval_ast(tree.body)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return f"O resultado é {result}."
        except Exception as exc:  # noqa: BLE001 - deliberate broad catch for user feedback
            return f"Não consegui resolver a expressão: {exc}."

    def _extract_expression(self, query: str) -> str | None:
        cleaned = query.strip().lower()
        if cleaned.startswith("calc "):
            return cleaned[5:].strip()
        match = self.expression_pattern.search(cleaned)
        if not match:
            return None
        expression = match.group(1).strip().rstrip("?")
        return expression

    def _eval_ast(self, node: ast.AST) -> float:
        if isinstance(node, ast.Num):  # type: ignore[attr-defined]
            return node.n  # type: ignore[return-value]
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](self._eval_ast(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = self._eval_ast(node.left)
            right = self._eval_ast(node.right)
            return OPERATORS[type(node.op)](left, right)
        raise ValueError("Operação matemática não suportada.")


@dataclass
class KnowledgeBaseTool:
    """Responde perguntas com base em uma base de conhecimento local."""

    knowledge_path: Path
    name: str = "knowledge_base"
    description: str = "Responde perguntas sobre tecnologia usando uma base local."
    threshold: float = 0.5
    _knowledge: dict[str, str] | None = None

    def __post_init__(self) -> None:
        if not self.knowledge_path.exists():
            raise FileNotFoundError(f"Base de conhecimento não encontrada em {self.knowledge_path}")

    @property
    def knowledge(self) -> dict[str, str]:
        if self._knowledge is None:
            with self.knowledge_path.open("r", encoding="utf-8") as fp:
                self._knowledge = json.load(fp)
        return self._knowledge

    def can_handle(self, query: str) -> bool:
        normalized = query.strip().lower()
        keywords = ("o que", "como", "por que", "para que", "qual")
        return any(normalized.startswith(keyword) for keyword in keywords)

    def run(self, query: str, memory: Memory) -> str:
        topics = list(self.knowledge.keys())
        match = get_close_matches(query.lower(), topics, n=1, cutoff=self.threshold)
        if not match:
            return (
                "Ainda não tenho essa informação na minha base. "
                "Você pode reformular a pergunta ou registrar para treinamento futuro."
            )
        topic = match[0]
        answer = self.knowledge[topic]
        return f"{answer}\n\n(Fonte: base de conhecimento local sobre '{topic}'.)"


def default_tools(data_dir: Path) -> Iterable[Tool]:
    """Convenience helper to build the default toolset."""

    knowledge_tool = KnowledgeBaseTool(knowledge_path=data_dir / "knowledge_base.json")
    return [MathTool(), knowledge_tool]
