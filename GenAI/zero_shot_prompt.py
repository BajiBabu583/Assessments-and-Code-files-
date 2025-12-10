from fastapi import FastAPI

from pydantic import BaseModel

from google import genai

app=FastAPI()

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-flash-lite")

My_AI=genai.Client(api_key=API)

class Validation(BaseModel):
    user_prompt:str


@app.post('/zero-shot')

def zero_shot(input:Validation):
    ans=My_AI.models.generate_content(

        model=MODEL,
        contents=input.user_prompt,
        config=(
            {
                "system_instruction":"You are an AI assistant just give the summary of the users prompt" }

        )
    )

    return ans.text