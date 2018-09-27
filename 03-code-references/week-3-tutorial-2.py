import csv
import requests
from bs4 import BeautifulSoup

url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"

response = requests.get(url)
html = response.content


soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())


table = soup.find('tbody', attrs={'class': 'stripe'})
# print(table.prettify())

list_of_rows = []
for row in table.findAll('tr'): # converting rows of the table into a list
    list_of_cells = [] # creating an empty list so we can put the data that we found in it, to eventually generate .csv file
    for cell in row.findAll('td'): # this embedded loop, goes over the 'row' which contains all the 'tr' tags, and gets 'td' tags
        text = cell.text.replace('\n\xa0Details\n', '') # getting the text, and then replacing the unnecessary part with nothing
        list_of_cells.append(text) # putting the data we just looped through and gathered, the text, inside empty lists 

    list_of_rows.append(list_of_cells) # putting all of the lists inside a larger list called list_of_rows

# print(list_of_rows)

# to write to a file, in this case to a csv file, we need to import the csv module first
# then, we're creating a new file and feeding it to csv module, and then using its writerows function

outfile = open("./inmates.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
