from flask import Flask
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def webscrap():
    url = requests.get('https://www.etvbharat.com/hi/state/shahdol-gym-dispute-fight-over-playing-obscene-music-young-men-beat-up-another-man-madhya-pradesh-news-mps26012701375').text
    soup = BeautifulSoup(url, 'lxml')
    news= soup.find('div',class_='__className_8df048')
    # print(news.prettify())
    headline = news.find('script', type='application/ld+json')

    data = json.loads(headline.string)

    headline = data["headline"]
    article = data["articleBody"]
    headline = headline.replace("।", "।\n\n")
    text = (
            f"Headline: {headline}\n"
            f"Article: {article}"
    
    )
    return text

if __name__ == "__main__":
    app.run()
