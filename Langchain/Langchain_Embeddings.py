import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
 
load_dotenv()
GOOGLE_API_KEY = os.getenv("API")
 
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")
 
outputs = embeddings.embed_query("This is an example for embeddings")
 
print(outputs[:10])