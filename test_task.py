# tests/test_task.py

from fastapi.testclient import TestClient  ## TestClient is used testing client based on requests,used to stimulate api calls without running oon server
from main import app  ##geting app from main file

client = TestClient(app)## creating test client that call API end points like .post(),.get()

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list) #assert checks whether the statement is true if false raise assertionError

def test_create_task():
    payload = {"title": "Test task", "completed": False}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test task"
    assert data["completed"] == False
    assert "id" in data

def test_get_task_by_id():
    # Create task first to get a valid ID
    payload = {"title": "Temporary Task"}
    create_response = client.post("/tasks", json=payload)
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_update_task():
    payload = {"title": "Task to Update"}
    created = client.post("/tasks", json=payload).json()
    task_id = created["id"]

    updated_payload = {"title": "Updated Task", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=updated_payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["completed"] == True

def test_delete_task():
    payload = {"title": "Task to Delete"}
    created = client.post("/tasks", json=payload).json()
    task_id = created["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

    # Verify deletion
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404