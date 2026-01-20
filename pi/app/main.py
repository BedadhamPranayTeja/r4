from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
from .services.vision import VisionSystem

app = FastAPI()

# Enable CORS for React Frontend (default port 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Vision System
vision = VisionSystem()
vision.start()

# Store connected clients to broadcast CV commands
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error sending to client: {e}")
                # self.active_connections.remove(connection) # Don't remove while iterating!

manager = ConnectionManager()

# Background Task to Push CV Commands
@app.on_event("startup")
async def start_cv_broadcast():
    asyncio.create_task(cv_loop())

async def cv_loop():
    print("CV Loop Started")
    last_gesture = None
    
    while True:
        gesture, (vx, vy) = vision.get_control_data()
        
        payload = {"type": "control", "move": None, "look": None}
        
        # 1. Populate Active Command
        if gesture == "FIST":
            # Drive
            v = vy * 500  # Up is positive Y (Forward)
            w = vx * -1.5 # Reduced turn sensitivity
            payload["move"] = {"v": int(v), "w": float(w)}
            
        elif gesture == "PALM":
            # Look
            pan = vx * -90
            tilt = vy * 45
            payload["look"] = {"pan": int(pan), "tilt": int(tilt)}
        
        # 2. Handle Cleanup of Previous State (Safety Stop / Mode Switch)
        if gesture != last_gesture:
            if last_gesture == "FIST" and gesture != "FIST":
                # Stopped Driving -> Send Stop
                payload["move"] = {"v": 0, "w": 0}
                
            if last_gesture == "PALM" and gesture != "PALM":
                # Stopped Looking -> Center Camera
                payload["look"] = {"pan": 0, "tilt": 0}
                # Note: Comment out the line above to "Hold View" instead of centering.
                
            # print(f"Gesture Transition: {last_gesture} -> {gesture}")

        # 3. Broadcast if valid
        if payload["move"] or payload["look"]:
            # print(f"CV CMD: {gesture} {payload}")
            await manager.broadcast(payload)
            
        last_gesture = gesture
        await asyncio.sleep(0.05) # 20Hz Update


@app.get("/")
def read_root():
    return {"status": "r4_online"}

@app.get("/telemetry")
def read_telemetry():
    # Placeholder for IMU/Sensor data
    return {"pan": 0, "tilt": 0, "battery": 100}

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(vision.generate_frames(), 
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    print("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            # We receive commands from UI, but now we also SEND commands from CV
            # Ensure we don't create an infinite loop if UI echoes back
            # print(f"UI CMD: {data}")
            pass
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")
