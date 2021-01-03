from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://sports.news.naver.com/wfootball/index.nhn")
resp = html.get(url)

resp

