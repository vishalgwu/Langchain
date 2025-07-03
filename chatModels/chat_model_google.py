import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("✅ API Key Loaded:", api_key[:8] + "..." if api_key else "❌ None")

# Configure the client
genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel(model_name="models/gemini-pro")  # ✅ FULL NAME
    response = model.generate_content("What is the full name of Elon Musk?")
    print("✅ Gemini Response:", response.text)
except Exception as e:
    print("❌ ERROR:", e)

