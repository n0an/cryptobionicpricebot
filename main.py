from flask import Flask
from flask import request
from flask import jsonify
import requests
import json

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




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        # write_json(r)
        chat_id = r['message']['chat']['id']
        message_text = r['message']['text']

        if 'bitcoin' in message_text:
            send_message(chat_id, text='очень дорогой')


        return jsonify(r)
    return '<h1>Hello bot</h1>'

# Setting webhook url
# https://api.telegram.org/bot502455359:AAHlfIZenSBfeqieXn8maC4i1a032f6mNys/setWebhook?url=https://fec30acf.ngrok.io/

if __name__ == '__main__':
    app.run()
