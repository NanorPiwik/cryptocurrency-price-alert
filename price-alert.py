#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import requests
import schedule
import time

btc_eur = 'https://api.cryptonator.com/api/full/btc-eur'
eth_eur = 'https://api.cryptonator.com/api/full/eth-eur'
ltc_eur = 'https://api.cryptonator.com/api/full/ltc-eur'

ALERT_INTERVAL = 15

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def get_btc_eur():
    try:
        r = requests.get(btc_eur).json()
        price = int(float(r['ticker']['price']))
        return unicode(price)
    except:
        return '??'


def get_eth_eur():
    try:
        r = requests.get(eth_eur).json()
        price = round(float(float(r['ticker']['price'])), 1)
        return unicode(price)
    except:
        return '??'


def get_ltc_eur():
    try:
        r = requests.get(ltc_eur).json()
        price = round(float(float(r['ticker']['price'])), 2)
        return unicode(price)
    except:
        return '??'


def send_notification():
    message = 'BTC: '+get_btc_eur()+'  | '+'ETH: '+get_eth_eur()+'  |  '+'LTC: '+get_ltc_eur()
    sendmessage(message)

if __name__ == '__main__':
    schedule.every(ALERT_INTERVAL).minutes.do(send_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)

