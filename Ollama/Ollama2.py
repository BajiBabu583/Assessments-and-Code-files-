from ollama import ChatResponse

from ollama import chat

user_prompt=input("Ask Ollamma")

ans:ChatResponse=chat(

    model="gemma3:1b",messages=[{
        "role":"user",
        "content":user_prompt
    }]
)

print(ans.message.content)