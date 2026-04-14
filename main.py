from fpdf import FPDF

pdf = FPDF(orientation='P', format='A4', unit='mm')


pdf.add_page()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 12, txt='Apa kabar!!!', align='C')
pdf.output("lembar.pdf")