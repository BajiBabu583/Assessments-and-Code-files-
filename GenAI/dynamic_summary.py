from fastapi import FastAPI

from pydantic import BaseModel

from google import genai




app=FastAPI()

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")
MODEL=("gemini-2.5-pro")

My_AI=genai.Client(api_key=API)

class Baji(BaseModel):
    user_prompt:str
    system_prompt:str


@app.post('/prompt')
def get_ai(baji:Baji):
    ans=My_AI.models.generate_content(
        model=MODEL,
        contents=baji.user_prompt,

        config=
        (
            {
                "system_instruction":baji.system_prompt
            }
        )
    )    

    return ans.text