from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# This program does three things:

# 1. Opens the URL http://olympus.realpython.org/profiles/dionysus by using urlopen() from the urllib.request module

# 2. Reads the HTML from the page as a string and assigns it to the html variable

# 3. Creates a BeautifulSoup object and assigns it to the soup variable

print(soup.get_text())

soup.find_all("img")
