import time
import json
import requests
import logging
import atexit

from flask import jsonify, make_response
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

auth=('rpc', 'x')
headers = {
    'content-type': 'text/plain;',
}


@app.route("/blockchaininfo")
def main():
    payload = '{"jsonrpc":"1.0","method":"getblockchaininfo"}'
    response = requests.post('http://10.7.0.11:10340/', headers=headers, data=payload, auth=auth)
    return 'blockchaininfo'


@app.route("/logs")
def logs():
    return 'logs'


def mine_one_block_first_node():
    payload = '{"jsonrpc":"1.0","method":"generate","params":[1]}'
    response = requests.post('http://10.7.0.11:10340/', headers=headers, data=payload, auth=auth)
    print(response.json()['result'])


def mine_one_block_second_node():
    payload = '{"jsonrpc":"1.0","method":"generate","params":[1]}'
    response = requests.post('http://10.7.0.12:10340/', headers=headers, data=payload, auth=auth)
    print(response.json()['result'])



scheduler = BackgroundScheduler()
scheduler.add_job(func=mine_one_block_first_node, trigger="interval", seconds=2)
scheduler.add_job(func=mine_one_block_second_node, trigger="interval", seconds=3)
scheduler.start()



atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="19000")


