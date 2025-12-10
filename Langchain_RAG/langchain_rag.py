import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("MODEL")

# Initialize LLM    
llm = ChatGoogleGenerativeAI(
    model=MODEL,
    google_api_key=GOOGLE_API_KEY
)

file_path = "BajiBabu_Resume.pdf"

def create_rag_chain(path: str):
    print("Loading the PDF...")
    loader = PyPDFLoader(path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    texts = text_splitter.split_documents(documents)
    print(f"Document loaded and split into {len(texts)} chunks.")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=embeddings
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    print("Vector Store created. Retrieval readiness achieved.")

    template = """
    You are a helpful assistant. Use the following document excerpts to answer the question.
    If you don't find an answer in the context, say "I couldn't find that information in the document."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain

qa_chain = create_rag_chain(file_path)

question = input("Ask your question: ")
result = qa_chain.invoke({"query": question})

print("\nAnswer:")
print(result["result"])
