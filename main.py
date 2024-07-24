import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
filepaths = glob.glob('invoices/*.xlsx')
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr,date = filename.split('-')
    pdf.set_font("Times",size=16,style='B')
    pdf.cell(200, 10, txt="Invoice nr"+invoice_nr, ln=True, align='L')
    pdf.output("PDFs/"+filename+".pdf")