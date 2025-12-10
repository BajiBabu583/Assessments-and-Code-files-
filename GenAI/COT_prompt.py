from fastapi import FastAPI 

from pydantic import BaseModel

from google import genai

app=FastAPI()

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-pro")

My_AI=genai.Client(api_key=API)

class Validation(BaseModel):
    user_prompt:str

@app.post('/cot')
def cot_prompt():
    ans=My_AI.models.generate_content(
       model=MODEL,
       contents= "Anjaneyulu is husband of Anjamma, Anjamma is mother Baji.now tell me the relation between Anjaneyulu and Baji",
    
    )
    return ans.text


