from langchain_google_genai import GoogleGenerativeAIEmbeddings

llm=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

Query=llm.embed_query("India is the 4th largest Economic country in the world")

print(Query[:10])