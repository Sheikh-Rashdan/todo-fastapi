from typing import Any

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