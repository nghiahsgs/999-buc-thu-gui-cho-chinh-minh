from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("Five Short Plays.pdf", "rb"))



list_page = [0,1,2,3,5]

output = PdfFileWriter()
for i in list_page:
    output.addPage(inputpdf.getPage(i))

with open("reading_day1.pdf", "wb") as outputStream:
    output.write(outputStream)

