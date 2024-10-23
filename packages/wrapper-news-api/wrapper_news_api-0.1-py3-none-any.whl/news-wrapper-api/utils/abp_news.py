from bs4 import BeautifulSoup
import requests

def abp_news():
    try:
        content = requests.get('https://www.abplive.com/news').content
        soup = BeautifulSoup(content,'html.parser')

        news = []

        for i in soup.findAll('a',attrs={'class':'sub-news-story'}):
            title = i.find('div',class_='story-title').text
            url = i['href']
            data = {
                'title':title,
                'url':url
            }

            news.append(data)
            return news
    except Exception as e:
        return e