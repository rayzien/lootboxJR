"""
Configuration specific to the commands module.
"""

# Define any command-specific settings here
COMMAND_PREFIX = "/"

# List of allowed commands or enabled features
ENABLED_COMMANDS = [
    "start",
    "stop",
    "status",
    "help"
]

# Command timeouts (in seconds)
DEFAULT_TIMEOUT = 30

class CommandConfig:
    def __init__(self):
        self.prefix = COMMAND_PREFIX
        self.enabled = ENABLED_COMMANDS
        self.timeout = DEFAULT_TIMEOUT

    def is_enabled(self, command_name: str) -> bool:
        return command_name in self.enabled

command_config = CommandConfig()
