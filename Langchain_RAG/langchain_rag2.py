from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
API = os.getenv("API")
MODEL = os.getenv("MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# Load PDF
loader = PyPDFLoader("BajiBabu_Resume.pdf")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=API)

# Store to Chroma DB
vector_db = Chroma.from_documents(docs, embeddings)

# Retriever
retriever = vector_db.as_retriever(search_kwargs={"k": 2})

# LLM
llm = ChatGoogleGenerativeAI(model=MODEL, google_api_key=API)

# Correct Prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI assistant. Use ONLY the information in the context to answer.
If the question is not related to the document, reply:
"Sorry, because of my limitations I couldn't get the information."

Context:
{context}

Question:
{question}

Answer:
"""
)

# RAG Chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
    input_key="question",  # important fix!
    return_source_documents=False
)

# Ask user
while True:
    question = input("Ask your question (or type 'exit'): ")
    if question.lower() == "exit":
        break

    result = chain.invoke({"question": question})
    print("\nAnswer:", result["result"], "\n")
