"""
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API")
Model=os.getenv("MODEL1")

gemini = genai.Client(api_key=api_key)

response = gemini.models.generate_content(
    model=Model,
    contents="I want to know the history of India"
)

print(response.text)

"""


from google import genai


priya= "gemini-2.5-flash"

baji="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA"

AI=genai.Client(api_key=baji)

answer=AI.models.generate_content(
    model=priya,
    contents="I want to know who is the winner of 2022 T20 world cup"
)

print(answer.text)