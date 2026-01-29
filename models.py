from pydantic import BaseModel

class Task(BaseModel) : 
	id : int
	title : str
	compeleted : bool=False

class CreateTask(BaseModel) : 
	title:str