from fpdf import FPDF
import subprocess


class PDF(FPDF):
    def header(self):
        self.set_font('times', 'B', 20)

        self.cell(0, 14, 'Groups', border=False, ln=1, align='C')

        self.ln(20)


def make_pdf(groups):
    pdf = PDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('times', '', 10)

    for i, group in enumerate(groups):
        pdf.cell(0, 7, f"{i + 1}", ln=True, border=True)
        for person in group:
            pdf.cell(0, 7, f"{person[0]}", ln=True)

    pdf.output('groepjes.pdf')
    subprocess.Popen('groepjes.pdf', shell=True)
