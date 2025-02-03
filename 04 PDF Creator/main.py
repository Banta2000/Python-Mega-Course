from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv", index_col=0)

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

pdf.output("output.pdf")
