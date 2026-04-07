import google.generativeai as genai
import os
import sys

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Please set GEMINI_API_KEY environment variable. For testing, I'll just print out standard known names.")
    sys.exit()

genai.configure(api_key=api_key)

try:
    print("Available Models for generateContent:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
except Exception as e:
    print(f"Error: {e}")
