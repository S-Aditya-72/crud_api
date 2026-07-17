from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": True},
    {"id": 3, "title": "Learn FastAPI", "done": False}
]


@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})


@app.post("/tasks", status_code=201)
def create_task(task_data: dict):

    if "title" not in task_data or task_data["title"] == "":
        return JSONResponse(status_code=400, content={"error": "Task title is required"})

    new_id = len(tasks) + 1

    new_task = {"id": new_id, "title": task_data["title"], "done": False}
    tasks.append(new_task)

    return new_task
