from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("4000 english words volume 1-ebook.pdf", "rb"))



# list_page = [0,1,2,3,5]

# output = PdfFileWriter()
# for i in list_page:
#     output.addPage(inputpdf.getPage(i))

# with open("reading_day1.pdf", "wb") as outputStream:
#     output.write(outputStream)



nb_day = 1
page_start = 0
page_end = page_start+1 # moi trang 1 lan cat

# list_page = [0,1,2,3,5]
list_page = list(range(page_start,page_end))
output = PdfFileWriter()
for i in list_page:
    output.addPage(inputpdf.getPage(i))

with open("reading_day%s.pdf"%nb_day, "wb") as outputStream:
    output.write(outputStream)


for nb_day in range(2,191):
    # nb_day = 3
    page_start = page_end
    page_end = page_start+1 # moi trang 1 lan cat

    # list_page = [0,1,2,3,5]
    list_page = list(range(page_start,page_end))
    output = PdfFileWriter()
    for i in list_page:
        output.addPage(inputpdf.getPage(i))

    with open("reading_day%s.pdf"%nb_day, "wb") as outputStream:
        output.write(outputStream)
