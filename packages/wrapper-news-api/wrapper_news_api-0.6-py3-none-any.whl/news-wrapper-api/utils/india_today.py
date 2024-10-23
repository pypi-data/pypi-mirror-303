from bs4 import BeautifulSoup
import requests

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