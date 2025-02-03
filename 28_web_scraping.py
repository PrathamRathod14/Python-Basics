# Web scraping using requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/JSON"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print("Page title:", soup.title.string)