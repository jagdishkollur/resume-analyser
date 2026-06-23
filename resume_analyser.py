from dotenv import load_dotenv
from google import genai
import os

load_dotenv(".env")

# Read resume file
with open("resume.txt", "r", encoding="utf-8") as f:
    resume = f.read()

# Create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Prompt
prompt = f"""
Act as a recruiter.

Analyse this resume and give:

1. Key strengths
2. Weaknesses
3. One suggestion to improve it

Resume:
{resume}
"""

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)