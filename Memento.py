"""

definition: Memento: take a snapshot of an object's state so you
can restore it later (undo), without exposing internal details

"""

from __future__ import annotations
from dataclasses import dataclass


# -------- Memento (snapshot) --------
@dataclass(frozen=True, slots=True)
class EditorMemento:
    text: str
    cursor: int


# -------- Originator --------
class Editor:
    def __init__(self) -> None:
        self.text = ""
        self.cursor = 0

    def insert(self, s: str) -> None:
        self.text = self.text[:self.cursor] + s + self.text[self.cursor:]
        self.cursor += len(s)

    def move_cursor(self, pos: int) -> None:
        self.cursor = max(0, min(pos, len(self.text)))

    def save(self) -> EditorMemento:
        return EditorMemento(self.text, self.cursor)

    def restore(self, m: EditorMemento) -> None:
        self.text = m.text
        self.cursor = m.cursor


# -------- Caretaker (history) --------
class History:
    def __init__(self) -> None:
        self._stack: list[EditorMemento] = []

    def push(self, m: EditorMemento) -> None:
        self._stack.append(m)

    def pop(self) -> EditorMemento | None:
        return self._stack.pop() if self._stack else None


if __name__ == "__main__":
    ed = Editor()
    hist = History()

    hist.push(ed.save())
    ed.insert("hello")
    hist.push(ed.save())
    ed.insert(" world")
    print(ed.text, ed.cursor)

    m = hist.pop()
    if m: ed.restore(m)
    print(ed.text, ed.cursor)