import requests
import csv
from bs4 import BeautifulSoup

#Scrapying multiple pages.

#Create  a file to write to, add headers row
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []
# Collect and parse first page
for i in range(1 , 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser') 
##Remive bottom Links
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

# Pull all text from the BodyText div
#Pull text from all instances of <a> tag within BodyText div
    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a') 
#Use .contents to pull out the <a> tag's children and assoaciated href tags
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        print(names)
        print(links)
        
#Add each artist's name and associated link to a row
        f.writerow([names, links])