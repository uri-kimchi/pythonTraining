import csv
import PyPDF2


#  another git test
with  open ( '//home/urik/Documents/SOW008.005b ExecSum.pdf', mode ='rb') as pdff:
    pdfText = PyPDF2.PdfFileReader(pdff)
    x = pdfText.documentInfo
    with open ('/home/urik/Python38/workspace/extractedPDF.txt', 'w') as exFile:
        for i in range(len(x)-1):
            pdfPage = pdfText.getPage(i)
            pageText = pdfPage.extractText()
            exFile.write('This is Page {}\n'.format(i+1))
            exFile.write('=============================')
            exFile.write(pageText)

