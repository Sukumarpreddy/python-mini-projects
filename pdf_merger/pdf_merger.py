import PyPDF2
import os

pdfs = ['file1.pdf','file2.pdf',]

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()