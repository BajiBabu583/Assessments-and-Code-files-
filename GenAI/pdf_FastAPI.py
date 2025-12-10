from fastapi import FastAPI 

from pydantic import BaseModel

from google import genai

app=FastAPI()

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")
MODEL=("gemini-2.5-flash-lite")

My_AI=genai.Client(api_key=API)

PDF_PATH="BajiBabu_Resume.pdf"

UPLOAD_PDF=My_AI.files.upload(file=PDF_PATH)

@app.post('/upload-file')
def upload_file():
    ans=My_AI.models.generate_content(
        model=MODEL,
        contents=UPLOAD_PDF,
        config={
            "system_instruction":"You have to give the summarization for the user provided PDF"
        }

    )

    return ans.text