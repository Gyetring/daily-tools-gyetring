from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["Personal_Statement.pdf",
             "Grade_Report.pdf", "TOEFL.pdf"]:
    merger.append(pdf)

merger.write("out-basic.pdf")