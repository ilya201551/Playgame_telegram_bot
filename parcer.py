import requests
from bs4 import BeautifulSoup as bs
import collections


Game = collections.namedtuple('Game', ['title', 'price', 'link_', 'seller'])


class NewGames:
    DOMAIN_NAME = 'https://playgame.by/index.php?act=allsells&type=0'
    HEADERS = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3'
    }
    titles = []
    prices = []
    links = []
    sellers = []
    session = requests.Session()
    request = session.get(DOMAIN_NAME, headers=HEADERS)
    soup = bs(request.content, 'html.parser')
    products_table = soup.find('table')
    products = products_table.find_all('tr', attrs={'class': ['rowA', 'rowB']})
    for product in products:
        titles.append(product.find_all('a')[1].text)
        prices.append(int(product.find('div', attrs={'class': 'price'}).text))
        links.append('https://playgame.by/' + product.find_all('a')[1]['href'])
        sellers.append(product.find_all('a')[2].text[2:])
    

    def __init__(self):
        self.games = [Game(title, price, link_, seller)
                      for title, price, link_, seller in zip(self.titles, self.prices, self.links, self.sellers)]

    def __len__(self):
        return len(self.games)

    def __getitem__(self, position):
        return self.games[position]


def creating_suitable_prices():
    session = requests.Session()
    request = session.get('https://spreadsheets.google.com/feeds/list' +
                          '/1Lscd6K7wVHbD5kUHBhXnecxCayknR8sIFy-dtS2Wny4/od6/public/values?alt=json',
                          headers=NewGames.HEADERS)
    table_json = request.json()
    table_len = len(table_json['feed']['entry'])
    titles = [table_json['feed']['entry'][title]['gsx$games']['$t'] for title in range(table_len)]
    prices = [int(table_json['feed']['entry'][price]['gsx$prices']['$t']) for price in range(table_len)]
    suitable_prices = {title: price for title, price in zip(titles, prices)}
    return suitable_prices


outdated_proposals = []


def check_the_entry(game):
    if game.title in creating_suitable_prices()\
            and game.price <= creating_suitable_prices()[game.title]\
            and (game.seller + game.title) not in outdated_proposals:
        outdated_proposals.append(game.seller + game.title)
        return True
