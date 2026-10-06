from fastapi import APIRouter, Query, Depends, HTTPException
from models.todo_models import *
import storage.todo_storage as todo_storage

todo_router = APIRouter(prefix="/todos", tags=["todos"])

@todo_router.get("", response_model=list[TodoModel])
def get_todos(limit: int | None = Query(None, ge=1), db = Depends(todo_storage.get_db)):
    return todo_storage.get_todos(db, limit)

def validate_todo(todo_id: int, db = Depends(todo_storage.get_db)):
    todo = todo_storage.get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@todo_router.get("/{todo_id}", response_model=TodoModel)
def get_todo(todo = Depends(validate_todo), db = Depends(todo_storage.get_db)):
    return todo

@todo_router.post("", response_model=TodoModel, status_code=201)
def post_todo(todo_create: TodoCreate, db = Depends(todo_storage.get_db)):
    return todo_storage.add_todo(db, todo_create.model_dump())

@todo_router.delete("/{todo_id}", status_code=204)
def delete_todo(todo = Depends(validate_todo), db = Depends(todo_storage.get_db)):
    todo_storage.remove_todo(db, todo)

@todo_router.patch("/{todo_id}", response_model=TodoModel)
def patch_todo(todo_patch: TodoPatch, todo = Depends(validate_todo), db = Depends(todo_storage.get_db)):
    patched_todo = {k:v for k,v in todo_patch.model_dump().items() if v is not None}
    return todo_storage.patch_todo(db, todo, patched_todo)