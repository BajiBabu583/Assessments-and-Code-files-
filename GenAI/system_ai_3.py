import os

from dotenv import load_dotenv

from google import genai

load_dotenv()

API_KEY=os.getenv("API")
MODEL=os.getenv("MODEL1")

My_AI=genai.Client(api_key=API_KEY)

content=input("Let AI know about your query: \n")

response=My_AI.models.generate_content(
    model=MODEL,
    contents=content,
    config=(
        {"system_instruction":"You are a good and positive AI,you always give answers in the positive manner for the user questions"}

    )
)
print(response.text)