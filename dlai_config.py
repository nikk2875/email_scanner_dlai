import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Define input/output
GMAIL_FOLDER = os.getenv("GMAIL_FOLDER", "INBOX")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
OUTPUT_FOLDER = "output"

# Define providers URL
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Set API keys
openai_api_key = os.getenv('OPENAI_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# Define models
OPENAI_MODEL = "gpt-6-luna"
OPENROUTER_MODEL = "z-ai/glm-5.3"