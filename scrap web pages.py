import bs4
import requests
import re

#
Current_URL = 'http://books.toscrape.com/catalogue/category/books_1/page-{}.html'
for i in range (1,5):
    req = requests.get (Current_URL.format(i))
    page  = bs4.BeautifulSoup (req.text,'lxml')
    pods = page.select('.product_pod')
    j = 0
    for pod in pods:
        j += 1
        stars = pod.select('.star-rating.Two')
        if (len(stars)>0):
            print ('page: {} product: {}'.format(i,j))
            p = pod.select('.product_price')[0]
            pp = p.select ('p')[0] 
            price = pp.select('.price_color')
            print (' Title: {} >>> Costs {}'.format(pod.select('a')[1]['title'], pp.text[2:]))



