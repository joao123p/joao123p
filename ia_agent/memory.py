"""Conversation memory for the simple I.A. agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass
class Message:
    """Represents a single message in the conversation."""

    role: str
    content: str


@dataclass
class Memory:
    """Stores the conversation context for the agent."""

    messages: List[Message] = field(default_factory=list)
    max_messages: int = 20

    def add_message(self, message: Message) -> None:
        """Add a new message to the memory, trimming old entries if necessary."""

        self.messages.append(message)
        if len(self.messages) > self.max_messages:
            overflow = len(self.messages) - self.max_messages
            del self.messages[0:overflow]

    def extend(self, messages: Iterable[Message]) -> None:
        """Extend memory with multiple messages."""

        for message in messages:
            self.add_message(message)

    def get_recent(self, limit: int = 5) -> List[Message]:
        """Return the most recent messages."""

        return self.messages[-limit:]

    def last_user_message(self) -> str | None:
        """Return the content of the last user message, if any."""

        for message in reversed(self.messages):
            if message.role == "user":
                return message.content
        return None

    def summary(self) -> str:
        """Return a lightweight summary of the conversation."""

        summary_lines = []
        for message in self.get_recent(limit=min(5, len(self.messages))):
            summary_lines.append(f"{message.role}: {message.content}")
        return " | ".join(summary_lines)
