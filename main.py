from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import re
import secrets

from flask_sslify import SSLify

app = Flask(__name__)

sslify = SSLify(app)

token = secrets.token

URL = 'https://api.telegram.org/bot' + token + '/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='blablabla', keyboard=None):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    if keyboard:
        answer['reply_markup'] = keyboard
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

    try:
        price = r[-1]['price_usd']
        return price
    except KeyError:
        print('price parsing error')

    # write_json(r.json(), filename='price.json')

def get_main_keyboard():
    reply_markup = { 'keyboard': [[{'text': '/bitcoin'}, {'text': '/ethereum'}, {'text': '/ripple'}]]}
    return reply_markup


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        # write_json(r)
        chat_id = r['message']['chat']['id']

        try:
            message_text = r['message']['text']
        except KeyError:
            print('error message text parsing')
            return jsonify(r)

        pattern = r'/\w+'

        if re.search(pattern, message_text):
            if message_text == r'/start':
                send_message(chat_id, text='Choose cryptocurrency', keyboard=get_main_keyboard())
            else:
                price = get_price(parse_text(message_text))
                send_message(chat_id, text=price, keyboard=get_main_keyboard())

        return jsonify(r)
    return '<h1>Hello bot</h1>'

# # Setting webhook url to localhost using ngrok app
# https://api.telegram.org/botTOKEN/setWebhook?url=https://fec30acf.ngrok.io/

if __name__ == '__main__':
    app.run()
