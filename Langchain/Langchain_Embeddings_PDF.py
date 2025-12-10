from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.document_loaders import PyPDFLoader

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_core.messages import HumanMessage

PDF=PyPDFLoader("BajiBabu_Resume.pdf")

PDF_Loader=PDF.load()

PDF_Text="\n".join([page.page_content for page in PDF_Loader])

LLM=GoogleGenerativeAIEmbeddings(model="gemini-2.5-pro",google_api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")



LLM2=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

Embed=LLM2.embed_query(PDF_Text)

print(Embed[:10])