import PyPDF2
import os

merger = PyPDF2.PdfMerger()
file_list = os.listdir("file") #Lista os arquivos na pasta file
file_list.sort() #Ordena os arquivos
print(file_list)

for file in file_list:
    if ".pdf" in file:
        merger.append(f'file/{file}')

merger.write('pdf_mesclado.pdf')