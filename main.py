import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    filename = Path(filepath).stem
    invoice_nr,date = filename.split('-')
    
    pdf.set_font("Times",size=16,style='B')
    pdf.cell(200, 10, txt="Invoice nr "+invoice_nr, ln=1, align='L')
    pdf.cell(200, 10, txt="Date "+date, ln=True, align='L')
    
    
    #content
    print(df)
    pdf.set_font("Times",size=12,style='B')
    pdf.cell(40, 10, txt="Product ID", ln=False, align='L',border=1)
    pdf.cell(50, 10, txt="Product Name", ln=False, align='L',border=1)
    pdf.cell(30, 10, txt="Amount", ln=False, align='L',border=1)
    pdf.cell(40, 10, txt="Price per Unit", ln=False, align='L',border=1)
    pdf.cell(30, 10, txt="Total Price", ln=True, align='L',border=1)
    total =0
    for idx,row in df.iterrows():
        pdf.set_font("Times",size=12)
        pdf.cell(40, 10, txt=str(row["product_id"]), ln=False, align='L',border=1)
        pdf.cell(50, 10, txt=row["product_name"], ln=False, align='L',border=1)
        pdf.cell(30, 10, txt=str(row["amount_purchased"]), ln=False, align='L',border=1)
        pdf.cell(40, 10, txt=str(row["price_per_unit"]), ln=False, align='L',border=1)
        pdf.cell(30, 10, txt=str(row["total_price"]), ln=True, align='L',border=1)
        total += row["total_price"]
    
    pdf.cell(40, 10, txt=" ", ln=False, align='L',border=1)
    pdf.cell(50, 10, txt=" ", ln=False, align='L',border=1)
    pdf.cell(30, 10, txt=" ", ln=False, align='L',border=1)
    pdf.cell(40, 10, txt=" ", ln=False, align='L',border=1)
    pdf.cell(30, 10, txt=str(total), ln=True, align='L',border=1)

    pdf.ln(3)
    pdf.set_font("Times",size=12,style='B')
    pdf.cell(200, 10, txt=f"The total due amount is {total} Euros.", ln=1, align='L')
    pdf.ln(1)
    pdf.cell(25, 8, txt="PythonHow", style='B', ln=False)
    pdf.image("pythonhow.png", w=10,)
    pdf.output("PDFs/"+filename+".pdf")