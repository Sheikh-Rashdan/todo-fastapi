from sqlalchemy import Engine, create_engine, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Any

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str|None] = mapped_column(String, nullable=True)


engine: Engine = create_engine("sqlite:///database/todos.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# Remove Later
todos: dict[int,Any] = {}
next_index: int = 1

def get_todos() -> list[dict[int,Any]]:
    return list(todos.values())

def get_todo(todo_id: int) -> dict[int,Any] | None:
    return todos.get(todo_id)

def add_todo(todo: dict[int,Any]) -> dict[int,Any]:
    global next_index
    todo["id"] = next_index
    todos[next_index] = todo
    next_index += 1
    return todo

def remove_todo(todo_id: int):
    del todos[todo_id]

def patch_todo(todo_id: int, patched_todo: dict[int,Any]):
    todo = get_todo(todo_id)
    todo |= patched_todo