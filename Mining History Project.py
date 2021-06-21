import requests
from bs4 import BeautifulSoup as bs
import sys
import io
from io import StringIO
from PyPDF2 import PdfFileReader
import PyPDF2 as pdf2



page = requests.get("https://www.recensio.net/rezensionen/zeitschriften/sehepunkte/13/07_08/mexiko-und-das-pazifische-asien-in-der-fra1-4hen/")
#https://www.recensio.net/front-page
soup = bs(page.text, "html.parser")

p = soup.find_all()
list_of_pdf = []

for link in p:

    list_of_pdf.append(link.get("href"))

print(list_of_pdf)

#response = requests.get(list_of_pdf[0])
"""
with io.BytesIO(response.content) as f:
    pdf = PdfFileReader(f)
    number_of_pages = pdf.getNumPages()
    newText = ""
    for i in range(0, number_of_pages):
        page1 = pdf.getPage(i)
        text = page1.extractText().split()
        for j in text:
            newText = newText + j + " "
    #print(newText)

    information = pdf.getDocumentInfo()

finaltext = newText.split()
print(finaltext)
"""