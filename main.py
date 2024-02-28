from threading import Thread

from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
import asyncio
from telethon.sync import TelegramClient

api_id = 1234
api_hash = ''

app = Flask(__name__)


def verif(username, code):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = TelegramClient('my_session', api_id, api_hash, loop=loop, system_version="4.16.30-vxCUSTOM")
    client.start()
    client.send_message(username, code)
    client.run_until_disconnected()


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    username = data['username']
    code = data['code']
    verif(username, code)
    return jsonify({'success': True})


def run_flask():
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()


if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    flask_thread.join()
