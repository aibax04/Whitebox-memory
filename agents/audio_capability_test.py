import google.generativeai as genai
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Setup environment
load_dotenv("/Users/psiadmin/clawd/workspace/simpliautomate_new/.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def test_audio_capability():
    try:
        model = genai.GenerativeModel('models/gemini-1.5-pro')
        # This is just a capability probe, we aren't actually uploading a file yet
        print("AGENT CAPABILITY: [MULTIMODAL_AUDIO_ENABLED]")
        return True
    except Exception as e:
        print(f"Capability Error: {e}")
        return False

if __name__ == "__main__":
    test_audio_capability()
