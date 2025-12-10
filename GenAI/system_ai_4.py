import os

from dotenv import load_dotenv

from google import genai
load_dotenv()
API_KEY=os.getenv("API")
MODEL=os.getenv("MODEL")

system_prompt=input("Give the rules to AI: \n")

user_prompt=input("Ask AI about your doubts : \n")

My_AI=genai.Client(api_key=API_KEY)
try:
    answer=My_AI.models.generate_content(

        model=MODEL,
        contents=user_prompt,
        config=
        {

          "system_instruction":system_prompt,
          "max_output_tokens":50

        }    
)

    print(answer.text)
finally:
    My_AI.close()