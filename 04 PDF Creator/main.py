from fpdf import FPDF
import pandas as pd
from get_invoices import read_files


def ex1():
    df = pd.read_csv("topics.csv", index_col=0)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=15)

    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=24)

        # Set the header
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for i in range(row["Pages"] - 1):
            pdf.add_page()

            # Set the footer
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

    pdf.output("output.pdf")


def print_invoice(name, data):
    name = name.replace(".xlsx", "")
    invoice_nr = name.split("-")[0]
    date = name.split("-")[1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", style="B", size=18)

    # Print the table header
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=10, txt=f"Invoice Nr {invoice_nr}", align="L", ln=1)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(w=0, h=8, txt=f"Date {date}", align="L", ln=1)
    pdf.ln(10)

    # Print the table header
    pdf.set_font("Arial", style="B", size=10)
    pdf.cell(25, 8, "ID", 1)
    pdf.cell(50, 8, "Name", 1)
    pdf.cell(25, 8, "Amount", 1, align="R")
    pdf.cell(25, 8, "Unit Price", 1, align="R")
    pdf.cell(25, 8, "Total", 1, align="R")
    pdf.ln()

    # Print the table
    for idx, row in data.iterrows():
        pdf.set_font("Arial", style="", size=10)
        pdf.cell(25, 8, str(row["product_id"]), 1)
        pdf.cell(50, 8, str(row["product_name"]), 1)
        pdf.cell(25, 8, str(row["amount_purchased"]), 1, align="R")
        pdf.cell(25, 8, str(row["price_per_unit"]), 1, align="R")
        pdf.cell(25, 8, str(row["total_price"]), 1, align="R")
        pdf.ln()

    # Print Total Sum Row
    pdf.set_font("Arial", style="B", size=11)
    pdf.cell(25, 8, "Total", 1, align="L")
    total_sum = data["total_price"].sum()
    pdf.cell(125, 8, str(total_sum), 1, align="R")
    pdf.ln(20)

    pdf.set_font("Arial", style="B", size=11)
    pdf.cell(125, 8, f"The total amount is: {total_sum} USD", 0, align="L")

    pdf.output(f"output/{name}.pdf")


data = read_files()
for filename, invoice_items in data.items():
    print_invoice(filename, invoice_items)
