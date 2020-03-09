import time
import json
import requests
import logging
import atexit
import os

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
    print('mined one block on first node')
    


def mine_one_block_second_node():
    payload = '{"jsonrpc":"1.0","method":"generate","params":[1]}'
    response = requests.post('http://10.7.0.12:10340/', headers=headers, data=payload, auth=auth)
    print('mined 1 block on 2nd node ')




def get_new_address_first():
    pass

def get_new_address_second():
    pass

def send_from_first_to_second():
    pass

def send_from_second_to_first():
    pass


def combined_send():
    payload = '{"jsonrpc":"1.0","method":"getnewaddress"}'
    response = requests.post('http://10.7.0.11:10340/', headers=headers, data=payload, auth=auth)
    address_first_node = response.json()['result']
    print('got new address 1st: ' + address_first_node)

    payload = '{"jsonrpc":"1.0","method":"getnewaddress"}'
    response = requests.post('http://10.7.0.12:10340/', headers=headers, data=payload, auth=auth)
    address_second_node = response.json()['result']
    print('got new address 2nd: ' + address_second_node)


    payload = '{"jsonrpc":"1.0","method":"sendtoaddress","params":["' + address_second_node + '", 1]}'
    response = requests.post('http://10.7.0.11:10340/', headers=headers, data=payload, auth=auth)
    print('send from 1 to 2 ')

    payload = '{"jsonrpc":"1.0","method":"sendtoaddress","params":["' + address_first_node + '", 1]}'
    response = requests.post('http://10.7.0.12:10340/', headers=headers, data=payload, auth=auth)
    print('send from 2 to 1 ')


estimatesmartfee = os.environ.get('ESMART_FEE')

scheduler = BackgroundScheduler()
scheduler.add_job(func=mine_one_block_first_node, trigger="interval", seconds=2)
scheduler.add_job(func=mine_one_block_second_node, trigger="interval", seconds=3)
if estimatesmartfee:
    scheduler.add_job(func=combined_send, trigger="interval", seconds=1)

scheduler.start()



atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="19000")


