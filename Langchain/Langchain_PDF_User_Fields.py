from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_core.messages import HumanMessage

from langchain_community.document_loaders import PyPDFLoader 

LLM=ChatGoogleGenerativeAI(model="gemini-2.5-pro",api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")


PDF=PyPDFLoader("BajiBabu_Resume.pdf")

Load_PDF=PDF.load()

PDF_Text="\n".join([page.page_content for page in Load_PDF])

user_field_1=input("Enter field 1: \n")
user_field_2=input("Enter field 2: \n")
user_field_3=input("Enter field 3: \n")

RES=HumanMessage(
    content=f"You are helpful assitant thet extracts the user needed information from the given here.{user_field_1}{user_field_2}{user_field_3}{PDF_Text}. Just give the asked information, if you don't know have the information just say, I don't have that information."
)

ans=LLM.invoke(RES)

print(ans)
