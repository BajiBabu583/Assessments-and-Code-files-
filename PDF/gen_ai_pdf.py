from google import genai

from fpdf import FPDF

pdf=FPDF()

input=input("Enter your text here which you want to convert into pdf \n")


# My model
API="AIzaSyCf886lqYag4TNTRQhy-VYQVXspm2h_PGI"
MODEL=("gemini-2.5-flash-lite")

MY_AI=genai.Client(api_key=API)



result=MY_AI.models.generate_content(
    model=MODEL,
    contents=input
)

result1=result.text


# add_page() function is used to add a new page to the pdf
pdf.add_page()

#set_font() function is used to set the font of the text
pdf.set_font("Arial", size=12)

#cell() function is used to add a cell to the pdf
for line in result1.split("\n"):
    pdf.cell(0,10,txt=line,ln=True)

pdf.output("result.pdf")    

MY_AI.close()