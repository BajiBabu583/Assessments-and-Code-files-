from fastapi import FastAPI 

from pydantic import BaseModel

from google import genai

app=FastAPI()

class Baji(BaseModel):
    user_prompt:str

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-flash")

My_AI=genai.Client(api_key=API)

@app.post('/entity')
def get_entity(baji:Baji):
    ans=My_AI.models.generate_content(
        model=MODEL,
        contents=baji.user_prompt,
        config=({
            "system_instruction":"You are an AI Assistant,You have to give the only 100 words description for the  "
        })

       )

    return ans.text

