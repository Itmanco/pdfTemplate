import glob
from pathlib import Path
from fpdf import FPDF


filespaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=14, style="B")
for filepath in filespaths:
    with open(filepath) as file:
        data = file.read()
        filename = Path(filepath).stem
        name = filename.split(".")[0]
        pdf.add_page()

        pdf.cell(w=20, h=16, txt=name.title(), )
        pdf.ln(16)
        pdf.multi_cell(w=160, h=8, txt=data)

pdf.output("PDFs/animals.pdf")