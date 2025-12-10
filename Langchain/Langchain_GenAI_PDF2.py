from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage

from langchain_community.document_loaders import PyPDFLoader

llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro",api_key="AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA")

PDF=PyPDFLoader("BajiBabu_Resume.pdf")

Load_PDF=PDF.load()

PDF_Text="\n".join([page.page_content for page in Load_PDF])

input1=input("Ask question : ")

res=HumanMessage(
    content={f"{input1}{PDF_Text}"}
)

ans=llm.invoke([res])

print(ans)

