from google import genai

API=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-flash-lite")

My_AI=genai.Client(api_key=API)

PDF_FILE="BajiBabu_Resume.pdf"

UPLOAD_PDF=My_AI.files.upload(file=PDF_FILE)



try:
    ans=My_AI.models.generate_content(
        model=MODEL,
        contents=UPLOAD_PDF,
        config=(
        {
            "system_instruction":"Give me the summarization for the provided pdf"
        }
    )
     )
    print(ans.text)

finally:
    My_AI.close()