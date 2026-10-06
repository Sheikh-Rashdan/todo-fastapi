from sqlalchemy import Engine, create_engine, String, select, delete, update
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Any, Generator

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str|None] = mapped_column(String, nullable=True)


engine: Engine = create_engine("sqlite:///database/todos.db")
SessionLocal = sessionmaker(bind=engine)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session,None,None]:
    db: Session = SessionLocal()
    try: yield db
    finally: db.close()

def get_todos(db: Session, limit: int|None = 0, category: str|None = None) -> list[Todo]:
    statement = select(Todo)
    if limit is not None:
        statement = statement.limit(limit)
    if category is not None:
        statement = statement.filter(Todo.category == category)

    result = db.execute(statement)
    todos = result.scalars().all()

    return todos

def get_todo(db: Session, todo_id: int) -> Todo | None:
    statement = select(Todo).where(Todo.id == todo_id)
    result = db.execute(statement)
    todo = result.scalar()

    return todo

def add_todo(db: Session, todo: dict[int,Any]) -> Todo:
    todo = Todo(**todo)

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo

def remove_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()

def patch_todo(db: Session, todo: Todo, patched_todo: dict[int,Any]) -> Todo:
    for attr, value in patched_todo.items():
        setattr(todo, attr, value)
    db.commit()
    db.refresh(todo)
    return todo