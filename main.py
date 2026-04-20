from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', format='A4', unit='mm')
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10,21,200,21)

    # set the footer
    pdf.ln(265)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(180,180,180)
    pdf.cell(0,10,row["Topic"], align='R')

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # set the footer
        pdf.ln(265)
        pdf.set_font('Arial', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, row["Topic"], align='R')

pdf.output("lembar.pdf")