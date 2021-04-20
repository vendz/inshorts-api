import requests
from bs4 import BeautifulSoup


def getNews(category):
    newsDictionary = {
        'success': True,
        'category': category,
        'data': []
    }

    try:
        if category != 'all':
            base_url = requests.get('https://www.inshorts.com/en/read/' + category)
        else:
            base_url = requests.get('https://www.inshorts.com/en/read/')

    except requests.exceptions.RequestException as e:
        newsDictionary['success'] = False
        newsDictionary['error'] = str(e)
        return newsDictionary

    soup = BeautifulSoup(base_url.text, 'lxml')
    news_cards = soup.find_all(class_='news-card')
    if not news_cards:
        newsDictionary['success'] = False
        newsDictionary['error'] = 'Invalid Category'
        return newsDictionary

    for index, card in enumerate(news_cards):
        try:
            title = card.find('div', class_="news-card-title").find('a').text.strip()
        except AttributeError:
            title = None

        try:
            content = card.find(class_="news-card-content").find('div').text
        except AttributeError:
            content = None

        try:
            img_url = card.find(class_="news-card-image")['style'].split("'")[1]
        except AttributeError:
            img_url = None

        try:
            read_more_url = card.find(class_="read-more").find('a').get('href')
        except AttributeError:
            read_more_url = None

        try:
            short_url = "https://inshorts.com" + card.find(class_="clickable").get('href')
        except AttributeError:
            short_url = None

        try:
            author = card.find(class_="author").text
        except AttributeError:
            author = None

        try:
            time = card.find(class_="time").text
        except AttributeError:
            time = None

        try:
            date = card.find(class_="date").text
        except AttributeError:
            date = None

        newsObject = {
            "title": title,
            "content": content,
            "img_url": img_url,
            "read_more_url": read_more_url,
            "short_url": short_url,
            "author": author,
            "date": date,
            "time": time
        }

        newsDictionary['data'].append(newsObject)
    return newsDictionary
