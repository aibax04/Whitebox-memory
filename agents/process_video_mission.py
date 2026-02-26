import google.generativeai as genai
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Setup environment
load_dotenv("/Users/psiadmin/clawd/workspace/simpliautomate_new/.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def process_video(file_path):
    print(f"Uploading file: {file_path}")
    video_file = genai.upload_file(path=file_path)
    print(f"Uploaded file '{video_file.display_name}' as: {video_file.uri}")

    while video_file.state.name == "PROCESSING":
        print('.', end='', flush=True)
        time.sleep(2)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)

    # Use 2.0 Flash for high-speed video analysis
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    
    prompt = """Watch this video carefully and extract any tasks, instructions, or observations. 
    If the user is showing a screen or a specific object, describe what is happening.
    Format the output as a clear mission brief."""
    
    print("\nAnalyzing video content...")
    response = model.generate_content([prompt, video_file])
    print("\n---MISSION_EXTRACTION---")
    print(response.text)
    print("---END---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_video(sys.argv[1])
