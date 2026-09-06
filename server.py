import time
import threading
import subprocess
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot_state = {
    "running": False,
    "selected_device": None,
    "stats": {"gold": 0, "elixir": 0, "attacks": 0, "walls": 0, "time_elapsed": 0},
    "logs": [],
    "config": {}
}

start_time = 0

def add_log(msg: str):
    ts = time.strftime("%H:%M:%S")
    entry = f"[{ts}] {msg}"
    bot_state["logs"].append(entry)
    print(entry)

def bot_loop():
    global start_time
    start_time = time.time()
    add_log("Bot worker loop started.")
    
    while bot_state["running"]:
        dev = bot_state["selected_device"]
        if not dev:
            add_log("Error: Target emulator disconnected.")
            break

        add_log("Scanning bases matching minimum loot...")
        time.sleep(3)

        if not bot_state["running"]:
            break

        add_log("Match found! Deploying troops...")
        time.sleep(5)

        bot_state["stats"]["gold"] += 450000
        bot_state["stats"]["elixir"] += 380000
        bot_state["stats"]["attacks"] += 1
        bot_state["stats"]["time_elapsed"] = int((time.time() - start_time) // 60)
        add_log("Raid ended: +450k Gold, +380k Elixir. Returning home.")
        time.sleep(6)

@app.get("/api/devices")
def get_devices():
    try:
        raw = subprocess.check_output(["adb", "devices"]).decode()
        devices = [line.split()[0] for line in raw.strip().split("\n")[1:] if "\tdevice" in line]
        return {"devices": devices}
    except Exception:
        return {"devices": []}

@app.post("/api/adb/restart")
def restart_adb():
    try:
        subprocess.run(["adb", "kill-server"])
        subprocess.run(["adb", "start-server"])
        return {"status": "restarted"}
    except Exception as e:
        return {"error": str(e)}

class StartRequest(BaseModel):
    device: str = "emulator-5554"

@app.post("/api/bot/start")
def start_bot(req: StartRequest):
    if not bot_state["running"]:
        bot_state["running"] = True
        bot_state["selected_device"] = req.device
        threading.Thread(target=bot_loop, daemon=True).start()
    return {"status": "started"}

@app.post("/api/bot/stop")
def stop_bot():
    bot_state["running"] = False
    add_log("Bot stopped by user.")
    return {"status": "stopped"}

@app.get("/api/stats")
def get_stats():
    return bot_state["stats"]

@app.get("/api/logs")
def get_logs():
    return {"logs": bot_state["logs"][-40:]}

@app.post("/api/config")
def set_config(cfg: dict):
    bot_state["config"] = cfg
    return {"status": "saved"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
