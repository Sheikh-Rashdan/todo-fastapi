from fastapi import APIRouter, Query, Depends, HTTPException
from models.todo_models import *
import storage.todo_storage as todo_storage

todo_router = APIRouter(prefix="/todos", tags=["todos"])

@todo_router.get("", response_model=list[TodoModel])
def get_todos(limit: int | None = Query(None, ge=1)):
    subtodos = todo_storage.get_todos()

    if limit is None:
        return subtodos
    
    return subtodos[:limit]

def validate_id(todo_id: int):
    if todo_storage.get_todo(todo_id) is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_id

@todo_router.get("/{todo_id}", response_model=TodoModel)
def get_todo(todo_id: int = Depends(validate_id)):
    return todo_storage.get_todo(todo_id)

@todo_router.post("", response_model=TodoModel, status_code=201)
def post_todo(todo_create: TodoCreate):
    todo = todo_storage.add_todo(todo_create.model_dump())
    return todo

@todo_router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int = Depends(validate_id)):
    todo_storage.remove_todo(todo_id)

@todo_router.patch("/{todo_id}", response_model=TodoModel)
def patch_todo(todo_patch: TodoPatch, todo_id: int = Depends(validate_id)):
    patched_todo = {k:v for k,v in todo_patch.model_dump().items() if v is not None}
    todo_storage.patch_todo(todo_id, patched_todo)
    return todo_storage.get_todo(todo_id)