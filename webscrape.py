from bs4 import BeautifulSoup
import requests

html = requests.get('https://santabarbara.craigslist.org/search/roo').text

soup = BeautifulSoup(html, 'lxml')

houses = soup.find_all('li', class_='result-row')

for house in houses:
    title = house.find('h3', class_= 'result-heading').text
    price = house.find('span', class_ = 'result-price').text.replace(' ', '')

    print(f'''
    House: {title}
    Price: {price}
        '''
        )



"""
with open('craigslist.html', 'r') as html_file:
    content = html_file.read()

    
    soup = BeautifulSoup(content, 'lxml')
    
    listing_card = soup.find_all('div', class_='result-info')
    
    listing_title = soup.find_all(class_='result-title hdrlnk')
    listing_price = soup.find_all(class_ = 'result-price')

    for card in listing_card:
        listing_name = card.h3.text
        
        print(listing_name)
        print(listing_price)
"""
