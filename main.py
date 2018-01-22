from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import re

app = Flask(__name__)

URL = 'https://api.telegram.org/bot502455359:AAHlfIZenSBfeqieXn8maC4i1a032f6mNys/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='blablabla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        # write_json(r)
        chat_id = r['message']['chat']['id']
        message_text = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message_text):
            price = get_price(parse_text(message_text))
            send_message(chat_id, text=price)

        return jsonify(r)
    return '<h1>Hello bot</h1>'

# Setting webhook url
# https://api.telegram.org/bot502455359:AAHlfIZenSBfeqieXn8maC4i1a032f6mNys/setWebhook?url=https://fec30acf.ngrok.io/

if __name__ == '__main__':
    app.run()
