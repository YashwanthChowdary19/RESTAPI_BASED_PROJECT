from fastapi import FastAPI, HTTPException, status
from models import Task, TaskCreate, TaskUpdate

app = FastAPI()

# In-memory storage
tasks: list[Task] = []


# ---------------- CREATE ----------------
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=False
    )
    tasks.append(new_task)
    return new_task


# ---------------- READ ALL ----------------
@app.get("/tasks")
def get_all_tasks():
    return tasks


# ---------------- READ ONE ----------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- UPDATE (FULL) ----------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.completed = False
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- UPDATE (PARTIAL) ----------------
@app.patch("/tasks/{task_id}")
def partial_update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            if updated_task.title is not None:
                task.title = updated_task.title
            if updated_task.completed is not None:
                task.completed = updated_task.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- DELETE ----------------
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return

    raise HTTPException(status_code=404, detail="Task not found")
