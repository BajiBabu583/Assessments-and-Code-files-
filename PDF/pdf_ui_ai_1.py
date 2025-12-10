import gradio as gr

from google import genai

from fpdf import FPDF

API="AIzaSyCf886lqYag4TNTRQhy-VYQVXspm2h_PGI"

MODEL="gemini-2.5-flash-lite"

def create_pdf(user_input):
    MY_AI=genai.Client(api_key=API)
    pdf_text=MY_AI.models.generate_content(
        model=MODEL,
        contents=user_input,
        config={"system_instruction":"You are a good AI assistant you have to generate the content as per user requirement as its required format with its sufficient content"}
    )

    text=pdf_text.text

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)

    for line in text.split("\n"):
        pdf.cell(0,10,txt=line,ln=True)

        filename="Result1.pdf"
        pdf.output(filename)
        return filename
    

UI=gr.Interface(
fn=create_pdf,
inputs=gr.Textbox(lines=4,label="Enter your text"),
outputs=gr.File(label="Download PDF"),
title="Input to LLM & LLM to PDF",
description="Give your input and model will convert into pdf"
)    

UI.launch()