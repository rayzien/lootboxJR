from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn

app = FastAPI(title="Owoloot")

@app.get("/", response_class=HTMLResponse)
async def read_home():
    # Read the content of the home.html file from the pages directory
    html_path = Path("pages/home.html")
    
    if not html_path.exists():
        return HTMLResponse(content="<h1>Error: pages/home.html not found</h1>", status_code=404)
        
    html_content = html_path.read_text(encoding="utf-8")
    return html_content

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
