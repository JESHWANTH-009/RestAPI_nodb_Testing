from fastapi import APIRouter,HTTPException 
from pip._internal.cli import status_codes

router=APIRouter()

tasks=[{"id":1,"title":"Learn REST",'compelted':True},
       {"id":2,"title":"learn AWS","completed":False},
       {"id":3,"title":"learn LAngchain","completed":False}]

@router.get("/tasks")
def get_tasks():
    return tasks

@router.get("/tasks/{tasks_id}")
def get_tasks(tasks_id:int): ## defining type of input id 
    for i in tasks:
        if i["id"]==tasks_id:
            return i
    raise HTTPException(status_code=404,detail="Task not found")

@router.post("/tasks")
def create_task(task:dict):
    task["id"]=len(tasks)+1
    tasks.append(task)
    return task

@router.put("/tasks/{task_id}")
def update_task(task_id:int,new_task:dict):
    for i in tasks:
        if i["id"]==task_id:
            i.update(new_task)  ## to update dictonary
            return i
    raise HTTPException(status_code=404,detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for index, task in enumerate(tasks):
        if task["id"]==task_id:
            deleted_task=tasks.pop(index)
            return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")
    
