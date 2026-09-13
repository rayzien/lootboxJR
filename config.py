import os

class Config:
    """
    Main application configuration.
    Reads from environment variables with sensible defaults.
    """
    APP_NAME = os.getenv("APP_NAME", "Owoloot")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    
    # Discord token for Discum (replace with your actual token in environment variables)
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "YOUR_DISCORD_TOKEN_HERE")
    
    # Add other global configuration variables here
    API_VERSION = "v1"

config = Config()
