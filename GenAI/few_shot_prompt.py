from fastapi import FastAPI

from pydantic import BaseModel

from google import genai

app=FastAPI()

class Validation(BaseModel):
    user_prompt:str

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-flash-lite")

My_AI=genai.Client(api_key=API)


@app.post('/few-shot')
def few_shot():
    ans=My_AI.models.generate_content(

        model=MODEL,
        contents=({"""
            "system_instruction":"1.Hello How are you! = Elaa unnaru"
                 "2.Where are you staying now? = Ippudu Ekkada untunnaru"
                 "3.How is your mother?= tell me the answer"
                 
                 """
            
        })
    )
    return ans.text