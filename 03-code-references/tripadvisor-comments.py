import requests
from bs4 import BeautifulSoup
import time


url = "https://www.tripadvisor.com/Attractions-g43323-Activities-Minneapolis_Minnesota.html"
# response = requests.get(url)
# data = response.content

# soup = BeautifulSoup(data, "html.parser")
# listing = soup.findAll('div', 'listing')  # this will give us an array/list of all the divs with class listing
# print("number of listings: ", str(len(listing)))

# for s in listing:
#     name = s.findChildren('a')[0].string.strip()  # [0] syntax selecting the first element on the resulting array/list
#     print('site name: ' + name)


# this function will download the webpage and return the data, the html
def featch(url):
    response = requests.get(url)
    data = response.content
    return data


# this function will pass in the html data we just got and extract certain elements out
def extract_data(data):
    name = data.findChildren('a')[0].string.strip()

    try:
        num_reviews = data.findChildren('span', 'more')[0].findChildren('a')[0].string.strip()
    except Exception as e:
        num_reviews = '0'

    print('site name: ' + name)
    print('number of reviews: ' + num_reviews)
    print('->')


# this ia a wrapper function that makes use of the above two function
def featch_items(url):
    page = featch(url)

    soup = BeautifulSoup(page, "html.parser")
    listing = soup.findAll('div', 'listing')

    for s in listing:
        extract_data(s)  # this will loop through all elements to get each elements

    print("1 sec to process...")
    time.sleep(1)  # after it gets all of the listings it'll pause for one sec

# featch_items(url)


# AUTOMATION

# putting two parts of the URL in two different strings
base_url = "https://www.tripadvisor.com/Attractions-g43323-Activities-oa"
city_url = "-Minneapolis_Minnesota.html#FILTERED_LIST"

page = featch(url)  # using the function to go to html and download it to memory
soup = BeautifulSoup(page, "html.parser")  # parsing using beau...s package


# using soup to find all elements in the div tag class pageNumbers, [0] selecting first element
# and within that class, all the a tags, and [-1] selecting the last item on the list
# getting the string from within that tag, and stripping it from spaces
num_page = soup.findAll('div', 'pageNumbers')[0].findAll('a')[-1].string.strip()

# converting the resulted string to an integer
num_page = int(num_page)
# print(num_page)


# looping through all elements
current_page = 0
for i in range(num_page):
    # adding two parts together with the inbetween number
    url = base_url + str(current_page) + city_url
    featch_items(url)  # making use of the wrapper function we created earlier

    current_page += 30  # incrementing the current_page by 30, for the new URL
