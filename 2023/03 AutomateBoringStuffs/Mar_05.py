""" 
Created on : 05/03/23 10:33 AM
@author : ds  
"""
import PyPDF2 as pdf
import os
from config import Flexi

# Get all the pdf files in the current working directory
pdf_files = []

for file in os.listdir(Flexi.pdffolder):
    if file.endswith('.pdf'):
        pdf_files.append(file)

pdf_files.sort(key=str.lower)
print(pdf_files)

pdf_writer = pdf.PdfWriter()

# Loop through all the pdf files
for file in pdf_files:
    pdf_file_obj = open(Flexi.pdffolder+file, 'rb')
    pdf_reader = pdf.PdfReader(pdf_file_obj)

    # Loop through all the pages and add them
    for page_num in range(0, len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        pdf_writer.add_page(page_obj)

    pdf_file_obj.close()

# Save the resulting pdf to a file
pdf_output = open(Flexi.pdffolder +'allinvoices.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
