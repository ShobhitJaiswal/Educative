import requests
from fake_useragent import UserAgent
## importing the beautifulsoup module
import bs4

## send a request and receive the information from https://www.google.com
response = requests.get("https://www.google.com")

## creating BeautifulSoup object
soup = bs4.BeautifulSoup(response.content, "html.parser")

## using 'prettify' method to print the content
print(soup.prettify())