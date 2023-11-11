from fastapi import FastAPI, WebSocket, UploadFile, File
import asyncio
import uuid
import simulate_classroom as sc

app = FastAPI()

# In-memory storage for tasks and file paths
tasks = {}

@app.post("/upload/")
async def upload_and_start_simulation(file: UploadFile = File(...)):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "status": "in progress",
        "result": None
    }
    asyncio.create_task(run_simulation(task_id, file.read()))
    return {"task_id": task_id, "message": "Simulation started"}

async def run_simulation(task_id: str, content: str):
    result = await sc.simulate_classroom(content)
    tasks[task_id]["status"] = "completed"
    tasks[task_id]["result"] = result

@app.websocket("/ws/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id: str):
    await websocket.accept()
    try:
        task = tasks.get(task_id)
        if not task:
            await websocket.send_text("Task not found")
            return
        while task["status"] == "in progress":
            await asyncio.sleep(1)
        await websocket.send_json(task["result"])
    finally:
        await websocket.close()