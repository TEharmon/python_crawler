#python_everyday_boannews.py
#매일 11시 23분마다 보안뉴스를 자동으로 크롤링하여 보여준다.


import schedule
import time
import requests
from bs4 import BeautifulSoup


def collect_news():
    main_url='http://www.boannews.com/search/news_hash.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED'
    res=requests.get(main_url)
    soup=BeautifulSoup(res.content, 'lxml')
    url='http://www.boannews.com'+soup.find(class_='news_list').find('a').get('href')
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'lxml')
    print(soup)
    print('********************************************************************')
    title=soup.find("div",{"id":"news_title02"}).text
    date=soup.find("div",{"id":"news_util01"}).text.strip()
    content=soup.find("div",{"id":"news_content"}).text
    print(title)
    print(date)
    print(content)




schedule.every().day.at("11:23").do(collect_news)


while True:
    schedule.run_pending()
    time.sleep(1)
