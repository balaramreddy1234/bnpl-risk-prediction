import os

# Get the absolute path of the backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths for all storage folders
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "bnpl.db")

# Use environment variable for security on Render
SECRET_KEY = os.environ.get("SESSION_KEY", "bnpl_ultra_secure_2026")

# Create all necessary directories immediately
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)