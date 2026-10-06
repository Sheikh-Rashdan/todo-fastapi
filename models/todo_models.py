from pydantic import BaseModel, ConfigDict

class TodoPatch(BaseModel):
    task: str | None = None
    category: str | None = None

class TodoCreate(BaseModel):
    task: str
    category: str | None = None

class TodoModel(TodoCreate):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: int