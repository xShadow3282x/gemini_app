from fastapi import FastAPI
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# Debugging: Print startup message
print("🚀 Starting FastAPI server...")

# Load .env file
load_dotenv()
API_KEY = ("AIzaSyDxyzGj8p4MqRWGqpAfFNCQLcWNUNh5aOg")

# Debugging: Check if API key is loaded
print(f"🔑 API Key Loaded: {API_KEY is not None}")

if not API_KEY:
    raise ValueError("❌ API key is missing! Make sure it's set in the .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Create FastAPI instance
app = FastAPI()  # Ensure 'app' is defined here

print("✅ FastAPI app initialized.")

# Pydantic model to validate the incoming request body
class RequestBody(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: RequestBody):
    print(f"📩 Received prompt: {request.prompt}")  # Debugging print
    response = model.generate_content(request.prompt)
    print(f"📝 Response: {response.text}")  # Debugging print
    return {"response": response.text}

import uvicorn

if __name__ == "__main__":
    print("🌍 Running Uvicorn...")
    # Remove --reload to avoid the error
    uvicorn.run("app:app", host="127.0.0.1", port=8000)

