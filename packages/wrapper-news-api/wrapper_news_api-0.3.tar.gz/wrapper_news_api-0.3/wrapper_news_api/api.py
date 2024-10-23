from bs4 import BeautifulSoup
import requests

class NewsAPI:
    def __init__(self):
        pass

    def abp():
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
        
    
def bbc(query=None):
    news = []
    base_url = 'https://www.bbc.com'

    try:
        if query:
            # Search BBC for the query
            url = f'{base_url}/search?q={query}'
        else:
            # Fetch BBC news homepage
            url = f'{base_url}/news'

        content = requests.get(url).content
        soup = BeautifulSoup(content, 'html.parser')

        # Extract news articles
        for i in soup.findAll('div', attrs={'data-testid': 'card-text-wrapper'}):
            title = i.h2.text if i.h2 else "No title"
            description = i.p.text if i.p else "No description"
            data = {
                "title": title,
                "description": description
            }
            news.append(data)

        return news

    except Exception as e:
        return {"error": str(e)}

    
def india_today():
    try:
        content = requests.get('https://www.indiatoday.in/').content
        soup = BeautifulSoup(content,'html.parser')

        news = []

        for i in soup.findAll('article',attrs={'class':'B1S3_story__card__A_fhi'}):
            data = {
                "title":i.a.text,
                "description":i.p.text,
            }
            news.append(data)
        return news
    except Exception as e:
        return e
