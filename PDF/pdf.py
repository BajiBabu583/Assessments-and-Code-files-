from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = """This is an example PDF generated using FPDF.
You can add multiple lines of text.
FPDF handles text wrapping manually, so we write line by line."""

for line in text.split("\n"):
    pdf.cell(0, 10, txt=line, ln=True)

pdf.output("output.pdf")
