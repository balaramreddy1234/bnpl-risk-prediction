import sqlite3
import os

# Local SQLite Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    # Check if we are in production (Render)
    db_url = os.environ.get("DATABASE_URL")
    
    if db_url:
        # Connect to PostgreSQL
        import psycopg2 # You will need to add 'psycopg2-binary' to requirements.txt
        from psycopg2.extras import RealDictRow
        conn = psycopg2.connect(db_url)
        # This makes Postgres behave like sqlite3.Row (access by column name)
        conn.cursor_factory = RealDictRow 
        return conn
    else:
        # Connect to local SQLite
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn