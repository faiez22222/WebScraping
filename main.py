import requests as r
from bs4 import BeautifulSoup as bs4 # import package
# provide the target url
resp = r.get('https://jobs.apple.com/en-gb/search')
soup = bs4(resp.content, "html.parser") # load the HTML content in parser


print(soup.find_all('a', class_='table--advanced-search__title'))