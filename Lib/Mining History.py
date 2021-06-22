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

p = soup.find_all('a')
list_of_pdf = []

for link in p:

    list_of_pdf.append(link.get('href'))

new_list = []
for i in range(0,len(list_of_pdf)):

    if list_of_pdf[i] != None:
        new_list.append(list_of_pdf[i])

last_list = []
for i in new_list:
    if "pdf" in i:
        last_list.append(i)

print(last_list)
response = requests.get(last_list[0])

with io.BytesIO(response.content) as f:
    pdf = PdfFileReader(f)
    number_of_pages = pdf.getNumPages()
    newText = ""
    for i in range(0, number_of_pages):
        page1 = pdf.getPage(i)
        text = page1.extractText().split()
        for j in text:
            newText = newText + j + " "
    print(newText)

    information = pdf.getDocumentInfo()

finaltext = newText.split()
print(finaltext)
