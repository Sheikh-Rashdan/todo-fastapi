# Todo FastAPI

A lightweight Todo API built with FastAPI, SQLAlchemy, and SQLite. It exposes CRUD-style endpoints for managing todo items and is ready to be used with a frontend such as a Vite/React app running on `http://localhost:5173`.

## Features

- Create, read, update, and delete todo items
- SQLite persistence via SQLAlchemy
- FastAPI automatic request validation
- CORS configured for local frontend development
- Optional category filtering when listing todos
- Simple project structure suitable for learning and extension

## Tech Stack

- Python 3.14+
- FastAPI
- SQLAlchemy
- SQLite

## Project Structure

```text
.
├── database/
│   └── todos.db              # SQLite database file
├── models/
│   └── todo_models.py        # Pydantic request/response models
├── routers/
│   └── todo_router.py        # Todo routes and validation
├── storage/
│   └── todo_storage.py       # SQLAlchemy models and database helpers
├── main.py                   # FastAPI application entry point
├── pyproject.toml            # Project metadata and dependencies
├── uv.lock                   # Locked dependency file
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.14 or newer
- `uv` (recommended, as this project includes a `uv.lock` file)

### Install dependencies

```bash
uv sync
```

If you are using the existing virtual environment instead of `uv`, make sure the project dependencies are installed there as well.

## Run the API

Start the FastAPI app with:

```bash
uv run uvicorn main:app --reload
```

The app will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

All todo routes are under the `/todos` prefix.

### Get all todos

```http
GET /todos
```

Optional query parameters:

```http
GET /todos?limit=10
GET /todos?category=work
GET /todos?limit=10&category=work
```

### Get a single todo

```http
GET /todos/{todo_id}
```

### Create a todo

```http
POST /todos
```

Request body:

```json
{
  "task": "Buy groceries",
  "category": "errands"
}
```

### Update a todo

```http
PATCH /todos/{todo_id}
```

Request body:

```json
{
  "task": "Buy groceries and vegetables",
  "category": "shopping"
}
```

### Delete a todo

```http
DELETE /todos/{todo_id}
```

## Example Requests

### Create a todo with curl

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"task":"Write project README","category":"documentation"}'
```

### List todos

```bash
curl "http://127.0.0.1:8000/todos"
```

### List todos filtered by category

```bash
curl "http://127.0.0.1:8000/todos?category=work"
```

### Update a todo

```bash
curl -X PATCH "http://127.0.0.1:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{"task":"Write project README and publish it"}'
```

## Database

This project uses SQLite with the database file stored at:

```text
database/todos.db
```

The database is automatically initialized on application startup via `init_db()` in `main.py`.

## Notes

- The app is configured to accept requests from `http://localhost:5173` for local frontend development.
- The root endpoint returns a simple JSON payload:

```json
{"about": "Todo API"}
```
