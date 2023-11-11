# Python (Server-side with FastAPI)
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/upload")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        # Process data asynchronously
        async for result in async_process_data(data):
            await websocket.send_text(result)

async def async_process_data(data):
    # Implement your asynchronous processing logic
    yield "Processing data..."
