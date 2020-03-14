from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(
    open("999 La Thu Gui Cho Chinh Minh - Mieu Cong Tu.pdf", "rb"))

dem=0
for i in range(2, inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("letters/letters%s.pdf" % dem, "wb") as outputStream:
        output.write(outputStream)
    dem+=1
