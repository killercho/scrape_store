'''
    Test
'''
# This is a test application testing what sites work with web scraping and what doesn'
# This confirms that SteamStore works with web scraping so that will be my project
# The user wants to check if a game is discounted so he enters the name of the game as an input
# Then the server makes a search in the steam store for that particular game and
# if it finds such a game it returns the game discounted and original price.
# If they are the same number just say that the game is not discounted yet and return only
# one of the numbers

# Problem is if the game is not currently lowered in price and
# if the game is not the first one to show up

import requests
from bs4 import BeautifulSoup

URL = 'https://store.steampowered.com/search/?term=red+dead+redemtion+3'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'lxml')

# print(page.text)
print(soup.find_all("div", class_="discount_final_price")[0])
print(soup.find_all("div", class_="discount_original_price")[0])
