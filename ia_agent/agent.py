"""High-level orchestration for the simple I.A. agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

from .memory import Memory, Message
from .tools import Tool, default_tools


@dataclass
class Agent:
    """Conversational agent com ferramentas e memória."""

    name: str = "Aurora"
    description: str = (
        "Agente virtual modular com memória curta e suporte a ferramentas especializadas."
    )
    memory: Memory = field(default_factory=Memory)
    tools: Sequence[Tool] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.tools:
            data_dir = Path(__file__).resolve().parent / "data"
            self.tools = tuple(default_tools(data_dir))

    def respond(self, user_input: str) -> str:
        """Processa a mensagem do usuário e produz uma resposta."""

        self.memory.add_message(Message(role="user", content=user_input))

        for tool in self.tools:
            if tool.can_handle(user_input):
                tool_response = tool.run(user_input, self.memory)
                self.memory.add_message(Message(role="assistant", content=tool_response))
                return tool_response

        fallback = self._generate_response(user_input)
        self.memory.add_message(Message(role="assistant", content=fallback))
        return fallback

    # ---------------------------------------------------------------------
    def _generate_response(self, user_input: str) -> str:
        """Resposta simples baseada na conversa recente."""

        last_user = self.memory.last_user_message()
        summary = self.memory.summary()
        base_response = (
            "Estou aqui para ajudar! Apesar de não ter uma resposta exata,"
            " posso orientar próximos passos."
        )
        hints = []
        if last_user:
            hints.append(f"Você comentou: '{last_user}'.")
        if summary:
            hints.append(f"Resumo recente: {summary}.")
        if hints:
            base_response += " " + " ".join(hints)
        base_response += " Se quiser, tente fazer uma pergunta começando com 'o que', 'como' ou 'qual'."
        return base_response

    def chat(self, prompts: Iterable[str]) -> Iterable[str]:
        """Gera respostas para uma sequência de mensagens."""

        for prompt in prompts:
            yield self.respond(prompt)

    def system_prompt(self) -> str:
        """Retorna a descrição usada pelo agente."""

        return f"{self.name}: {self.description}"
