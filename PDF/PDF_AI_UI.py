import gradio as gr
from google import genai
from fpdf import FPDF

API = "AIzaSyA-SsBef1O30YyaHmG6jigNjnTX2raliqA"
MODEL = "gemini-2.5-flash-lite"

def generate_pdf(user_input):
    try:
        # Call LLM
        with genai.Client(api_key=API) as client:
            result = client.models.generate_content(
                model=MODEL,
                contents=user_input
            )
        result_text = result.text

        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for line in result_text.split("\n"):
            pdf.cell(0, 10, txt=line, ln=True)

        # Save PDF
        filename = "result.pdf"
        pdf.output(filename)

        return filename  # Gradio will allow downloading

    except Exception as e:
        return f"Error: {e}"

# Gradio UI
ui = gr.Interface(
    fn=generate_pdf,
    inputs=gr.Textbox(lines=4, label="Enter your text"),
    outputs=gr.File(label="Download PDF"),
    title="LLM → PDF Generator",
    description="Enter text, the model will rewrite it and convert it into a PDF."
)

ui.launch()
