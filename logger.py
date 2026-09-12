import logging
import sys

class ColorfulFormatter(logging.Formatter):
    """Custom logging formatter for colorful output."""
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[1;91m' # Bold Red
    }
    RESET = '\033[0m'
    
    def format(self, record):
        # Create a copy to avoid mutating the original record for other handlers
        import copy
        record_copy = copy.copy(record)
        
        color = self.COLORS.get(record_copy.levelname, self.RESET)
        record_copy.levelname = f"{color}{record_copy.levelname}{self.RESET}"
        record_copy.msg = f"{color}{record_copy.msg}{self.RESET}"
        
        return super().format(record_copy)

def get_logger(name: str = "owoloot") -> logging.Logger:
    """
    Creates and returns a colorful configured logger instance.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        formatter = ColorfulFormatter(
            "\033[90m%(asctime)s\033[0m - \033[95m%(name)s\033[0m - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        
    return logger

log = get_logger()
