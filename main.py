from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
import uvicorn
import asyncio
from logger import log_history, log_subscribers
from config import config

app = FastAPI(title="Owoloot")

# Mount the common directory for static assets (js, css, images)
app.mount("/common", StaticFiles(directory="common"), name="common")

@app.get("/", response_class=HTMLResponse)
async def read_home():
    # Read the content of the home.html file from the pages directory
    html_path = Path("pages/home.html")
    
    if not html_path.exists():
        return HTMLResponse(content="<h1>Error: pages/home.html not found</h1>", status_code=404)
        
    html_content = html_path.read_text(encoding="utf-8")
    return html_content

bot_state = {
    "status": "running",  # "running", "hanged_up", "captcha_detected"
    "owo_balance": 1250450
}

@app.get("/api/status")
async def get_status():
    token = config.DISCORD_TOKEN
    masked_token = f"{token[:15]}...***" if len(token) > 15 else "Not Configured"
    return JSONResponse({
        "status": bot_state["status"],
        "account": masked_token,
        "owo_balance": bot_state["owo_balance"],
        "coins_formatted": f"{bot_state['owo_balance']:,}"
    })

@app.post("/api/status")
async def update_status(payload: dict):
    new_status = payload.get("status")
    if new_status in ["running", "hanged_up", "captcha_detected"]:
        bot_state["status"] = new_status
    if "owo_balance" in payload:
        try:
            val = int(payload["owo_balance"])
            bot_state["owo_balance"] = val
        except (ValueError, TypeError):
            pass
    return JSONResponse({
        "status": bot_state["status"],
        "account": f"{config.DISCORD_TOKEN[:15]}...***" if len(config.DISCORD_TOKEN) > 15 else "Not Configured",
        "owo_balance": bot_state["owo_balance"],
        "coins_formatted": f"{bot_state['owo_balance']:,}"
    })

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    # Send history first
    for msg in log_history:
        await websocket.send_text(msg)
    
    # Subscribe to new logs
    queue = asyncio.Queue()
    log_subscribers.append(queue)
    try:
        while True:
            msg = await queue.get()
            await websocket.send_text(msg)
    except WebSocketDisconnect:
        log_subscribers.remove(queue)

@app.get("/config", response_class=HTMLResponse)
async def read_config():
    html_path = Path("pages/config.html")
    if not html_path.exists():
        return HTMLResponse(content="<h1>Error: pages/config.html not found</h1>", status_code=404)
    return html_path.read_text(encoding="utf-8")

@app.get("/settings", response_class=HTMLResponse)
async def read_settings():
    html_path = Path("pages/settings.html")
    if not html_path.exists():
        return HTMLResponse(content="<h1>Error: pages/settings.html not found</h1>", status_code=404)
    return html_path.read_text(encoding="utf-8")

if __name__ == "__main__":
    print("Starting server... Access the app at http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
