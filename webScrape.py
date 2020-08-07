import bs4
import requests
import os

#------------------------------------------------------------
# Scraping site = toscrape.com
#------------------------------------------------------------

res = requests.get('https://www.ynet.co.il/home/0,7340,L-8,00.html')
#print (type(res))
#print (res.text)

resNice = bs4.BeautifulSoup(res.text,"lxml") 
for contextItem in resNice.select('.sub-title'):
    print (contextItem  )

""" 
print (resNice.select('h1'))
paragraphs = resNice.select('p')
for par in paragraphs:
    print ('_____________With Tags_______________________________')
    print (par)

for par in paragraphs:
    print ('_____________Text Neto _________________________________________')
    print (par.getText())
 """

"""
fl = open ('sampleHTML.html','r')
anotherExample = fl.read()
fl.close()

bsData = bs4.BeautifulSoup (anotherExample,'lxml')
print(bsData.select('title'))
xx = bsData.select('title')
for x in xx:
    print(type(xx))
    print(x.getText())

"""
