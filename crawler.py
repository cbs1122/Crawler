import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://sports.news.naver.com/wfootball/index.nhn")
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a'):
    print(link.text.strip(), link.get('href'))
