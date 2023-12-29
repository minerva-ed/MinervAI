from fastapi import FastAPI, WebSocket, UploadFile, File, Form
import asyncio
import uuid
import simulate_clients as sc
import prospect_generator as pg
from fastapi.middleware.cors import CORSMiddleware
import json
import utilities

# Initialize the FastAPI app
app = FastAPI()

# Configure Cross-Origin Resource Sharing (CORS) Middleware
# This configuration allows requests from any origin, with any method, and any header.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# In-memory dictionary to store the status and result of simulation tasks
tasks = {}

@app.post("/upload/")
async def upload_and_start_simulation(file: UploadFile = File(...), customers: str = Form(...)):
    """
    Endpoint to upload a file and start a simulation task.
    Generates a unique task ID for each upload and initiates an asynchronous simulation task.
    :param file: The file uploaded by the client.
    :return: A dictionary containing the task ID and a message indicating the simulation has started.
    """
    # Generate a unique ID for the task
    task_id = str(uuid.uuid4())

    # Initialize task status and result in the tasks dictionary
    tasks[task_id] = {
        "status": "in progress",
        "result": None
    }

    # Read and decode the content of the uploaded file
    content = await file.read()
    file_string = content.decode('utf-8')

    # Log file receipt and start the simulation in an asynchronous task
    asyncio.create_task(run_simulation(task_id, file_string, customers))
    
    return {"task_id": task_id, "message": "Simulation started"}

async def run_simulation(task_id: str, content: str, customers: str):
    """
    Asynchronous function to run the simulation.
    Updates the task's status and result in the global tasks dictionary upon completion.
    :param task_id: Unique ID of the task.
    :param content: Content of the uploaded file to simulate.
    """
    # Perform simulation and store the result
    result = await sc.simulate_clients(content, customers)
    tasks[task_id]["status"] = "completed"
    tasks[task_id]["result"] = result

@app.post("/customer-profiles/")
async def generate_customer_profiles(product_file: UploadFile = File(...), sales_profile: str = Form(...)):
    # product_details = await product_file.read()
    # print("generate profiles:", product_details, sales_profile)
    # return await pg.generate_prospects(product_details, sales_profile)
    with open('samples/sales/sample-customers.json', 'r') as f:
        data = json.load(f)
        return data

@app.websocket("/ws/sample")
async def sample_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        with open('samples/sales/sample-response.json', 'r') as f:
            data = json.load(f)
        await websocket.send_json(data)
    finally:
        print("sample websocket closing")
        await websocket.close()

    

@app.websocket("/ws/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id: str):
    """
    WebSocket endpoint to stream the status and result of the simulation task.
    :param websocket: The WebSocket connection instance.
    :param task_id: The task ID for which status and result are to be streamed.
    """
    await websocket.accept()
    try:
        # Retrieve the task based on task_id
        task = tasks.get(task_id)

        # Check if task exists and stream updates
        if not task:
            await websocket.send_text("Task not found")
            return
        while task["status"] == "in progress":
            print("in-progress")
            await asyncio.sleep(1)
        await websocket.send_json(task["result"])
    finally:
        # Close the WebSocket connection
        print("websocket closing")
        await websocket.close()
