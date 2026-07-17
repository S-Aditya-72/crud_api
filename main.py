from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
tasks = [
    {"id": 1, "name": "Apple", "in_stock": True},
    {"id": 2, "name": "Banana", "in_stock": False},
    {"id": 3, "name": "Cherry", "in_stock": True}
]


@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_single_item(item_id: int):
    # Now item_id is available as a normal integer inside this function!
    pass


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Item {task_id} not found"})
