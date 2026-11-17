
import os
from dotenv import load_dotenv

# Find the backend folder
BACKEND_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# Load variables from backend/.env
load_dotenv(os.path.join(BACKEND_DIR, ".env"))

# Read environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
