from google import genai

API_KEY=("AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

MODEL=("gemini-2.5-flash-lite")

SIVA=genai.Client(api_key=API_KEY)

try:

    answer=SIVA.models.generate_content(
    model=MODEL,
    contents="I want poem on Dhanuj",
    config={
        "max_output_tokens":50
    }
    )

    print(answer.text)

finally:
    SIVA.close()

