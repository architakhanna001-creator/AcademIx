import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", api_key is not None)

# Create Gemini client
client = genai.Client(api_key=api_key)

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what a Computer Network is in 5 simple lines."
)

print("\n========== GEMINI RESPONSE ==========\n")
print(response.text)