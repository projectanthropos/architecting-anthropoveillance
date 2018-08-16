from bs4 import BeautifulSoup
import urllib
import requests

start_url = 'https://www.alibaba.com/catalog/cctv-products_cid3011?spm=a2700.9161164.5.107.69954e02Yt6zN2'
data = urllib.request.urlopen(start_url).read()
soup = BeautifulSoup(data, 'html.parser')

titles = soup.select('h2.title a')
for title in titles:
    print(title.text)
