from langchain_classic.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os


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

    # Split text
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    texts = text_splitter.split_documents(documents)
    print(f"Document loaded and split into {len(texts)} chunks.")

    # Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    # Chroma vector DB
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding_function=embeddings   # FIXED
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    print("Vector Store created. Retrieval ready.")

    # Prompt
    template = """
    You are a helpful assistant. Use the following document excerpts to answer the question.
    If you don't find an answer in the context, say: "I couldn't find that information in the document."

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

    # RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        input_key="query",              # IMPORTANT for correct invocation
        return_source_documents=False
    )

    return qa_chain


# Initialize RAG
qa_chain = create_rag_chain(file_path)

# Ask a question
question = input("Ask your question: ")
result = qa_chain.invoke({"query": question})   # FIXED

print("\nAnswer:")
print(result["result"])
