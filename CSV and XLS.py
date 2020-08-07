import csv
import PyPDF2

with  open ( '/home/urik/Python38/Complete-Python-3-Bootcamp-master/15-PDFs-and-Spreadsheets/examplePIPE.csv' ,mode = 'r') as csvf:
    csvr = csv.reader(csvf,  delimiter = '|')
    the_lines = list(csvr)
    for csvl in csvr:
        print (csvl)
        # for word in csvl:
        #      print (word)
        #print (csvl[0])

#  another git test
with  open ( '//home/urik/Documents/SOW008.005b ExecSum.pdf', mode ='rb') as pdff:
    pdfText = PyPDF2.PdfFileReader(pdff)
    pdfText.pages
    pdfPage = pdfText.getPage(0)
    pageText = pdfPage.extractText()
    print (pageText)
    with open ('/home/urik/Python38/workspace/extractedPDF.txt', 'w+') as exFile:
        exFile.write(pageText)