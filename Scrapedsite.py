import requests
import csv
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

#Remive bottom Links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

#Create  a file to write to, add headers row
f = csv.writer(open('z-artist-names.csv','w'))
f.writerow(['Name', 'Link'])

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

#Pull text from all instances of <a> tag within BodyText div

artist_name_list_items = artist_name_list.find_all('a')

#Create for loop to print out all artists' names
#for artist_name in artist_name_list_items:
    #print(artist_name.prettify())

#Use .contents to pull out the <a> tag's children and assoaciated href tags
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archieve.org'+ artist_name.get('href')
    print(names)
    print(links)

    #Add each artist's name and associated link to a row
    f.writerow([names,links])

    