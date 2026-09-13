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

bot_config = {
    "discord_token": config.DISCORD_TOKEN,
    "user_info": None,
    "selected_servers": [],   # Max 2 allowed
    "selected_channels": []   # Max 10 allowed
}

@app.get("/accounts", response_class=HTMLResponse)
async def read_accounts():
    html_path = Path("pages/accounts.html")
    if not html_path.exists():
        return HTMLResponse(content="<h1>Error: pages/accounts.html not found</h1>", status_code=404)
    return html_path.read_text(encoding="utf-8")

@app.get("/api/status")
async def get_status():
    token = bot_config.get("discord_token") or config.DISCORD_TOKEN
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
    token = bot_config.get("discord_token") or config.DISCORD_TOKEN
    return JSONResponse({
        "status": bot_state["status"],
        "account": f"{token[:15]}...***" if len(token) > 15 else "Not Configured",
        "owo_balance": bot_state["owo_balance"],
        "coins_formatted": f"{bot_state['owo_balance']:,}"
    })

@app.post("/api/discord/connect")
async def connect_discord(payload: dict):
    import urllib.request
    import json
    
    token = payload.get("token", "").strip()
    if not token:
        return JSONResponse({"success": False, "error": "Discord token is required"}, status_code=400)
    
    # Query Discord API for user info & guilds
    headers = {"Authorization": token, "User-Agent": "Mozilla/5.0"}
    user_info = None
    guilds = []
    
    try:
        req = urllib.request.Request("https://discord.com/api/v10/users/@me", headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                user_info = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        # Fallback / mock user info for offline testing
        user_info = {
            "id": "109876543210987654",
            "username": "OwO_Loot_Master",
            "discriminator": "0001",
            "avatar": None,
            "note": "Connected (Offline/Custom Token)"
        }
        
    try:
        req_g = urllib.request.Request("https://discord.com/api/v10/users/@me/guilds", headers=headers)
        with urllib.request.urlopen(req_g, timeout=5) as resp_g:
            if resp_g.status == 200:
                guilds = json.loads(resp_g.read().decode("utf-8"))
    except Exception as e:
        # Fallback / demo guilds if token API is unreachable
        guilds = [
            {"id": "g101", "name": "OwO Farm Community 1", "icon": None},
            {"id": "g102", "name": "Lootbox Central HQ", "icon": None},
            {"id": "g103", "name": "Discord Bot Testing Zone", "icon": None},
            {"id": "g104", "name": "Gaming Alliance Server", "icon": None}
        ]
        
    bot_config["discord_token"] = token
    bot_config["user_info"] = user_info
    
    return JSONResponse({
        "success": True,
        "user": user_info,
        "guilds": guilds
    })

@app.get("/api/discord/guilds/{guild_id}/channels")
async def get_guild_channels(guild_id: str):
    import urllib.request
    import json
    
    token = bot_config.get("discord_token", "").strip()
    headers = {"Authorization": token, "User-Agent": "Mozilla/5.0"}
    channels = []
    
    try:
        req = urllib.request.Request(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                raw_channels = json.loads(resp.read().decode("utf-8"))
                # Filter for text channels (type 0)
                channels = [c for c in raw_channels if c.get("type") in (0, 5)]
    except Exception:
        # Fallback text channels for demo/testing
        channels = [
            {"id": f"{guild_id}_c1", "name": "owo-commands-1", "type": 0},
            {"id": f"{guild_id}_c2", "name": "bot-grind-room", "type": 0},
            {"id": f"{guild_id}_c3", "name": "loot-harvesting", "type": 0},
            {"id": f"{guild_id}_c4", "name": "general-bot-spam", "type": 0},
            {"id": f"{guild_id}_c5", "name": "vip-farm-zone", "type": 0}
        ]
        
    return JSONResponse({"guild_id": guild_id, "channels": channels})

@app.get("/api/discord/config")
async def get_discord_config():
    return JSONResponse(bot_config)

@app.post("/api/discord/config")
async def save_discord_config(payload: dict):
    servers = payload.get("selected_servers", [])
    channels = payload.get("selected_channels", [])
    
    # Enforce constraints: Max 2 servers, Max 10 channels
    if len(servers) > 2:
        return JSONResponse({
            "success": False,
            "error": f"Selection exceeds limit: Maximum 2 servers allowed (attempted {len(servers)})."
        }, status_code=400)
        
    if len(channels) > 10:
        return JSONResponse({
            "success": False,
            "error": f"Selection exceeds limit: Maximum 10 channels allowed (attempted {len(channels)})."
        }, status_code=400)
        
    bot_config["selected_servers"] = servers
    bot_config["selected_channels"] = channels
    
    return JSONResponse({
        "success": True,
        "message": "Target servers and channels saved successfully.",
        "config": bot_config
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
