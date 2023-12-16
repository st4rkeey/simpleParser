import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def parser(url: str) -> None:
    result = requests.get(url=url)
    soup = BeautifulSoup(result.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    for i in range(0, len(quotes)):
        writing_csv(quotes[i].text, authors[i].text, tags[i].text)

def writing_csv(*args: str) -> None:
    with open('file.csv', 'a') as f:
        for i in args:
            f.write(f'{i}\n')


if __name__ == '__main__':
    parser(url='https://quotes.toscrape.com/')