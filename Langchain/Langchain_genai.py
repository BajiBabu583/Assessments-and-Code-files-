from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage

llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro",api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

result=llm.invoke("Give me the best self introduction for BPO role")

print(result.content)