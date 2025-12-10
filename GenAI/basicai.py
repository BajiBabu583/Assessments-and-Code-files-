import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

api_key = os.getenv("API")
model_name = os.getenv("MODEL", "gemini-1.5-flash")

# Initialize client
client = genai.Client(api_key=api_key)

user_rules = input("Give your Rules: \n")
rules="You are a helpful assistant tha follows the given rules" 
rules += f"{user_rules}"


content=input("Enter your input :\n")

# Generate content
response = client.models.generate_content(
    model=model_name,
    contents=content,
    config=(
        {"system_instruction":rules}
    )
)

print(response.text)
