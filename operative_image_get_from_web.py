import bs4
import requests
import re

#
Current_URL = 'http://books.toscrape.com/catalogue/category/books_1/page-{}.html'
for i in range (1,50):
    req = requests.get (Current_URL.format(i))
    pods = bs4.BeautifulSoup (req.text,'lxml')
    j = 0
    for pod of pods:
        j += 1
        print ('page: {} product: {}'.format(i,j))

