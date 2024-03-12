import string
from http.client import HTTPException
import uvicorn
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, constr, field_validator, ValidationError,validator

app = FastAPI()


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: str
    id: int
    status: str

    @field_validator('status')
    def check_status(cls, status):
        if status not in ["open", "close"]:
            raise ValueError('error in status')
        return status


tasks = []

@app.get("/tasks")
async def get_Tasks():
    if not tasks:
        raise ValueError('error the array tasks is empty')
    return tasks

@app.post("/task/")
async def add_Task(task: Task):
    try:
        print("not dict", task)
        print(" dict", task.dict())

        tasks.append(task.dict())
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return task


@app.delete("/tasks/{id}")
async def deleteTask(id: int):
    try:
        global tasks
        tasks = [task for task in tasks if task['id'] != id]
    except Exception as e:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "Task deleted successfully"




@app.put("/task/{task_id}")
async def update_task(task_id: int, task: Task):
    global tasks
    for t in tasks:
        if t['id'] == task_id:
            t.update(task.dict())
            return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="oops... an error occurred")





if __name__ == "__main__":
    uvicorn.run("Sample:app", host="127.0.0.1",
                port=8000, reload=True)
