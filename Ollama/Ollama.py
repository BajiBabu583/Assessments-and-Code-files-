from ollama import chat 

from ollama import ChatResponse

Ans:ChatResponse=chat(
    model="gemma3:1b",messages=[

        {
            'role':'user',
            'content':'Give me the black side things about India'
        }
    ]
)
print(Ans.message.content)