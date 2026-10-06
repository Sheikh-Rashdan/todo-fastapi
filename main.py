from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.todo_router import todo_router

app = FastAPI()
app.include_router(todo_router)
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173"],
                   allow_credentials=True,
                   allow_headers=["*"],
                   allow_methods=["GET", "POST", "PATCH", "DELETE"],
                  )

@app.get("/")
def root():
    return {"about": "Todo API"}