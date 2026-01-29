from fastapi import FastAPI,status
from models import Task,CreateTask
from data import tasks

app = FastAPI()

@app.get("/")
def root():
	return {"message":"FastAPI server is running"}


@app.post("/tasks",status_code = status.HTTP_201_CREATED)
def createTask(task:CreateTask):
	new_task = Task(
		id = len(tasks)+1,
		title = task.title,
		completed = False
		)
	tasks.append(new_task)
	return new_task