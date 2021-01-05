# 한 페이지당 기사 20개

import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

TARGET_URL_BEFORE_PAGE_NUM = "https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N&view=text&page="


def get_link_from_news(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = 1 + i*1
        position = URL.index('e=')
        URL_with_page_num = URL[: position+1] + str(current_page_num) \
                            + URL[position+1 :]
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, "html.parser")
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)

def main(argv):
    if len(argv) != 2:
        print("python [모듈이름] [가져올 페이지 숫자] [결과 파일명]")
        return
    page_num = int(argv[1])
    output_file_name = argv[2]
    target_URL = TARGET_URL_BEFORE_PAGE_NUM
    output_file = open(output_file_name, 'w')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()
 
 
if __name__ == '__main__':
    main(sys.argv)
