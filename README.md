# LootboxJR

Welcome to **LootboxJR** — Real-time OwO Coins tracker and bot status monitoring system built with FastAPI, WebSocket stream, and zero-emoji glassmorphism UI.

## Key Features

- **Big OwO Coins Display**: Prominent live coin tracker hero display.
- **3 Status States**:
  - `◈ RUNNING`: Active harvesting status with green pulse glow.
  - `▲ HANGED UP`: Paused or disconnected warning state.
  - `⬡ CAPTCHA DETECTED`: Action required red alert notification.
- **Zero Emojis**: Strictly 0 emojis. All UI elements use clean geometric symbols (`◈`, `▲`, `⬡`, `◉`).
- **No-Refresh Live Updates**: Status changes, balance updates, and terminal log feeds update dynamically in real time without refreshing the web page.
- **FastAPI Backend**: Async REST API endpoints for status state toggling and WebSocket ANSI terminal feed.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

2. **Start the server:**
   ```bash
   python main.py
   ```

3. **Access the application:**
   - Home Dashboard: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Settings: [http://127.0.0.1:8000/settings](http://127.0.0.1:8000/settings)
   - Configuration: [http://127.0.0.1:8000/config](http://127.0.0.1:8000/config)

## License
MIT License - Educational and open-source project created by rayzien.

