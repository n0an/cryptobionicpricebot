import requests
from main import write_json
import re

def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    # print(crypto)
    return crypto[1:]


def get_price(crypto='bitcoin'):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price
    # write_json(r.json(), filename='price.json')

def main():
    # print(get_price())
    print(get_price(parse_text('сколько стоит /ethereum?')))

if __name__ == '__main__':
    main()
