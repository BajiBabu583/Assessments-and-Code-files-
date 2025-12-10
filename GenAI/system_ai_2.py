import os 

from google import genai

from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API")

Model=os.getenv("MODEL1")


My_AI=genai.Client(api_key=API_KEY)

response=My_AI.models.generate_content(
    model=Model,
    contents="I Want the dark history of India",

    config=({
        "system_instruction":"The answes should be between 2000 to 2020"
    }
    )
)

print(response.text)


