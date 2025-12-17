import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# =========================
# 1️⃣ DATABASE LOGGER (Normal FileHandler)
# =========================

# Create a custom logger for database
db_logger = logging.getLogger("database")
db_logger.setLevel(logging.WARNING)  
# Logs WARNING and above (WARNING, ERROR, CRITICAL)

# Create file handler (logs go to this file)
db_file_handler = logging.FileHandler("db.log", mode="a")
# mode="a" → append, mode="w" → overwrite

# Create formatter (how log message will look)
db_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Attach formatter to handler
db_file_handler.setFormatter(db_formatter)

# Attach handler to logger
db_logger.addHandler(db_file_handler)

# Write logs
db_logger.warning("Database warning")
db_logger.error("Database error")


# =========================
# 2️⃣ ROTATING FILE LOGGER (Size-based)
# =========================

# Create another logger
rot_logger = logging.getLogger("rotating_db")
rot_logger.setLevel(logging.INFO)

# Create rotating file handler
rot_handler = RotatingFileHandler(
    filename="db_rotate.log",
    maxBytes=2000,      # file rotates after 2KB
    backupCount=3       # keeps 3 old files
)

# Create formatter
rot_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Set formatter
rot_handler.setFormatter(rot_formatter)

# Attach handler to logger
rot_logger.addHandler(rot_handler)

# Write logs
rot_logger.info("Rotating log message")


# =========================
# 3️⃣ TIME-BASED LOGGER (Daily rotation)
# =========================

# Create auth logger
auth_logger = logging.getLogger("auth")
auth_logger.setLevel(logging.INFO)

# Create time-based rotating handler
time_handler = TimedRotatingFileHandler(
    filename="auth.log",
    when="D",        # D = daily
    interval=1,      # every 1 day
    backupCount=3    # keep last 3 log files
)

# Create formatter
time_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Set formatter
time_handler.setFormatter(time_formatter)

# Attach handler to logger
auth_logger.addHandler(time_handler)

# Write logs
auth_logger.info("Auth info message")
auth_logger.warning("Auth warning message")
