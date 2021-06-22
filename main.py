from dataclasses import dataclass

from flask import Flask, render_template, redirect, url_for
from newsapi import NewsApiClient
import data

app = Flask(__name__)
app.secret_key = 'mYAoTSUidztoGQpVrYDWK7punVjKk7Xw'

api_key = 'cc94518726cc4bf697c8fa9ad7df9f6f'


@dataclass
class NewsData:
    title: str
    description: str
    url: str
    url_to_image: str

    @classmethod
    def from_dict(cls, info):
        return cls(info['title'], info['description'], info['url'], info['urlToImage'])


# Init
news_api = NewsApiClient(api_key='cc94518726cc4bf697c8fa9ad7df9f6f')


# /v2/everything
all_articles = news_api.get_everything(q='covid',
                                       language='en',
                                       sort_by='relevancy',
                                       page=1,
                                       page_size=18)


@app.route('/')
def home():
    return render_template('home.html', title='Covid Response', active_page='home')


@app.route('/data')
def view_data():
    return render_template('data.html', title='Covid Response | Data', active_page='data')


@app.route('/news')
def news():
    news_list = []
    articles = all_articles['articles']
    for article in articles:
        news_list.append(NewsData.from_dict(article))
    return render_template('news.html', title='Covid Response | News', active_page='news', news_list=news_list)


@app.route('/update')
def update_data():
    data.update()
    global all_articles
    all_articles = news_api.get_everything(q='covid',
                                           language='en',
                                           sort_by='relevancy',
                                           page=1,
                                           page_size=18)
    return redirect(url_for('home'))


@app.route('/login')
def login():
    return render_template('login.html', title='Covid Response', active_page='login')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
