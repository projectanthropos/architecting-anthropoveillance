from bs4 import BeautifulSoup
import urllib
import requests
import time


def get_items(url):
  html = urllib.request.urlopen(url).read()

  soup = BeautifulSoup(html, 'html.parser')

  titles = soup.select('.hdrlnk')

  for title in titles:
    print(title.text.encode('utf8'))

base_url = "https://minneapolis.craigslist.org/search/sss?query="
currentpage = 0

while currentpage < 1000:
  url = base_url + str(currentpage)
  get_items(url)
  currentpage = currentpage + 100
  time.sleep(.1)
