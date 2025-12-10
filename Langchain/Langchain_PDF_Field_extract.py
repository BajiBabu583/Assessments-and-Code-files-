from langchain_google_genai import ChatGoogleGenerativeAI 

from langchain_community.document_loaders import PyPDFLoader

from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
import os

load_dotenv()

API=os.getenv("API")

MODEL=os.getenv("MODEL")


LLM=ChatGoogleGenerativeAI(model=MODEL,google_api_key=API)

PDF=PyPDFLoader("BajiBabu_Resume.pdf")

PDF_Load=PDF.load()


PDF_Text = "\n".join([page.page_content for page in PDF_Load])

Res=HumanMessage(
    content={
        f"You have to give the field and their entities from the given PDF {PDF_Text}"
    }

)

Ans=LLM.invoke([Res])

print(Ans.content)
