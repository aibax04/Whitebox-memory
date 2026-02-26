import google.generativeai as genai
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Setup environment
load_dotenv("/Users/psiadmin/clawd/workspace/simpliautomate_new/.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def process_audio(file_path):
    print(f"Uploading file: {file_path}")
    # Upload the file
    audio_file = genai.upload_file(path=file_path)
    print(f"Uploaded file '{audio_file.display_name}' as: {audio_file.uri}")

    # Wait for the file to be processed
    while audio_file.state.name == "PROCESSING":
        print('.', end='', flush=True)
        time.sleep(2)
        audio_file = genai.get_file(audio_file.name)

    if audio_file.state.name == "FAILED":
        raise ValueError(audio_file.state.name)

    # Use a model that supports audio
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    
    prompt = """Listen carefully to this audio and extract any tasks or instructions. 
    Format the output as a clear list of objectives. 
    If there are specific details (topics, names, platforms), include them."""
    
    print("\nAnalyzing audio content...")
    response = model.generate_content([prompt, audio_file])
    print("\n---MISSION_EXTRACTION---")
    print(response.text)
    print("---END---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_audio(sys.argv[1])
