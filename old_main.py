import os
import time
import json
import subprocess
import socketio

# Device & Server Configuration
DEVICE_ID = "raspi_cam_1"
WEBSOCKET_SERVER = "http://192.168.1.6:5000"  # Use HTTP instead of ws://

# Initialize SocketIO Client
sio = socketio.Client()

# Process variable for motion detection
PROCESS = None

def start_motion_detection():
    """Start the motion detection process if not already running."""
    global PROCESS
    if PROCESS is None or PROCESS.poll() is not None:
        print("🟢 Starting motion detection...")

        PROCESS = subprocess.Popen(["python3", "motion_camera.py"])

    else:
        print("✅ Motion detection is already running.")

def stop_motion_detection():
    """Stop the motion detection process."""
    global PROCESS
    if PROCESS is not None:
        print("🛑 Stopping motion detection...")
        PROCESS.terminate()
        PROCESS.wait()
        PROCESS = None
    else:
        print("❌ Motion detection is not running.")

@sio.event
def connect():
    """Handle successful connection."""
    print("✅ Connected to WebSocket server")
    sio.emit("register_device", {"device_id": DEVICE_ID})  # Send device ID

@sio.event
def disconnect():
    """Handle disconnection."""
    global PROCESS
    if PROCESS is not None:
        print("🛑 Stopping motion detection...")
        PROCESS.terminate()
        PROCESS.wait()
        PROCESS = None
    print("❌ Disconnected from WebSocket server")

@sio.on("settings_update")
def apply_settings(settings):
    """Apply server settings: Start/Stop Motion Detection, Sleep Timer."""
    print(f"📡 Received settings update: {settings}")
    action = settings.get("action")  # Extract action

    if action == "stop_camera":
        stop_motion_detection()

    elif action == "start_camera":
        start_motion_detection()

    elif action == "sleep_mode":
        duration = settings.get("sleep")
        if duration is not None and isinstance(duration, (int, float)) and duration > 0:
            print(f"😴 Sleeping for {duration} seconds...")
            stop_motion_detection()
            time.sleep(duration)
            print("⏰ Waking up!")
            start_motion_detection()
        else:
            print("⚠️ Invalid sleep duration received. Ignoring.")
def main():
    """Connect to the WebSocket server and keep the connection alive."""
    while True:
        try:
            sio.connect(WEBSOCKET_SERVER)
            sio.wait()
        except Exception as e:
            print(f"⚠️ Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    main()
