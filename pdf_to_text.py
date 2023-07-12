import PyPDF2

pdfFileObj = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
texts = pageObj.extractText()

#print(texts)

f = open('pdf_text.txt', 'w', encoding='utf-8')
f.writelines(texts)
f.close()
