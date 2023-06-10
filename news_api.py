import requests
import sys


api_key = "YOUR KEY"


def news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    news = requests.get(url).json()
    article = news["articles"]

    news_articles = []
    for arti in article:
        news_articles.append(arti['title'])

    for i in range((20)):
        print(i+1, news_articles[i])

    sys.stdout = open('news.txt', 'w')
    for news in news_articles:
        sys.stdout.write(news + '\n')
    sys.stdout.close()


news()
