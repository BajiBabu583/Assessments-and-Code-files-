from fastapi import FastAPI
from pydantic import BaseModel

from google import genai

app=FastAPI()

class Baji(BaseModel):
    user_prompt:str


API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")    
MODEL=("gemini-2.5-pro")

My_AI=genai.Client(api_key=API)


@app.post('/summary')
def get_summery(text:Baji):
    try:
        Ans=My_AI.models.generate_content(
        model=MODEL,
        contents=text.user_prompt,
        config=dict(
            {"system_instruction":"You are an AI assistant you have to summarize the user prompt"}
            )
           )
        return Ans.text
    
    finally:
        My_AI.close()