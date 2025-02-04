from fastapi import FastAPI
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Debugging: Print startup message
print("🚀 Starting FastAPI server...")

# Load .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

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

@app.post("/generate")
def generate_text(prompt: str):
    print(f"📩 Received prompt: {prompt}")  # Debugging print
    response = model.generate_content(prompt)
    print(f"📝 Response: {response.text}")  # Debugging print
    return {"response": response.text}

if __name__ == "__main__":
    import uvicorn
    print("🌍 Running Uvicorn...")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
