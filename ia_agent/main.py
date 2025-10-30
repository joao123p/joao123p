"""Ponto de entrada para interagir com o agente via linha de comando."""

from __future__ import annotations

import argparse
from typing import Iterable

from .agent import Agent


def run_interactive(agent: Agent) -> None:
    """Executa um loop interativo simples no terminal."""

    print(agent.system_prompt())
    print("Digite 'sair' para encerrar.\n")
    while True:
        try:
            user_input = input("Você: ")
        except EOFError:
            print("\nAté logo!")
            break
        if user_input.strip().lower() in {"sair", "exit", "quit"}:
            print("Até logo!")
            break
        response = agent.respond(user_input)
        print(f"{agent.name}: {response}\n")


def run_demo(agent: Agent) -> None:
    """Executa um roteiro demonstrativo não interativo."""

    prompts = [
        "qual a diferença entre ia fraca e forte?",
        "Como posso treinar um modelo pequeno?",
        "Quanto é 2 + 2 * 5?",
        "Obrigado!"
    ]
    for prompt in prompts:
        print(f"Você: {prompt}")
        answer = agent.respond(prompt)
        print(f"{agent.name}: {answer}\n")


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Agente de I.A. local simples")
    parser.add_argument(
        "--demo",
        action="store_true",
        help="executa uma conversa demonstrativa predefinida",
    )
    args = parser.parse_args(argv)

    agent = Agent()

    if args.demo:
        run_demo(agent)
    else:
        run_interactive(agent)


if __name__ == "__main__":
    main()
