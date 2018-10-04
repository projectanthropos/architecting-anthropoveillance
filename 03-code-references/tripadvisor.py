import requests
from bs4 import BeautifulSoup
import time

url = "https://www.tripadvisor.com/Attractions-g43323-Activities-Minneapolis_Minnesota.html"


def featch(url):
    response = requests.get(url)
    data = response.content
    return data


def extract_data(data):
    name = data.findChildren('a')[0].string.strip()

    try:
        num_reviews = data.findChildren('span', 'more')[0].findChildren('a')[0].string.strip()
    except Exception as e:
        num_reviews = '0'

    print('site name: ' + name)
    print('number of reviews: ' + num_reviews)
    print('->')


def featch_items(url):
    page = featch(url)

    soup = BeautifulSoup(page, "html.parser")
    listing = soup.findAll('div', 'listing')

    for s in listing:
        extract_data(s)

    print("1 sec to process...")
    time.sleep(1)


base_url = "https://www.tripadvisor.com/Attractions-g43323-Activities-oa"
city_url = "-Minneapolis_Minnesota.html#FILTERED_LIST"

page = featch(url)
soup = BeautifulSoup(page, "html.parser")

num_page = soup.findAll('div', 'pageNumbers')[0].findAll('a')[-1].string.strip()

num_page = int(num_page)

current_page = 0

for i in range(num_page):
    url = base_url + str(current_page) + city_url
    featch_items(url)

    current_page += 30
