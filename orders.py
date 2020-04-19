# Запуск - python3 index.py
import ssl
import time
import json
import requests
import urllib
import hmac, hashlib
import websocket
from pdb import set_trace as pause
from start_net import get_start_net

class Order_worker():
    # def __init__(self, bot):
    #     # pause()
    #     self.bot = bot

    #изначальная простановка ордеров
    def init_net(self,settings):
        ##для тестов
        settings={}
        settings['rate'] = 100
        settings['amount_btc']= 1
        settings['amount_usd']= 100 
        ##

        rate= settings['rate'] 
        amount_usd = settings['amount_usd'] 
        amount_btc = settings['amount_btc']

        start_net = get_start_net()
        current_limit_up = current_limit_down = rate
        # pause()
        #бежим по   нашему сетапу
        print('if price goes up:place limit orders:')
        total_btc= total_usd =0
        for step in start_net:
            # print(step)# {'order_number':1,'step':0.01, 'amount':0.025},
            # добавляем n% к текущей лимитке
            current_limit_up = current_limit_up + rate*int(step['step'])
            current_limit_down = current_limit_down - rate*int(step['step']) 

            #мертвая зона 1%
            if step['amount'] == 0:
                continue
            current_amount_btc = amount_btc*step['amount']
            current_amount_usd= amount_usd*step['amount']
            total_btc = total_btc + current_amount_btc
            total_usd = total_usd + current_amount_usd
            # print(total_usd)
            # print("we sell: {current_amount_btc} btc for usdt limit:{current_limit_up}".format(**locals()))
            print("we buy for {current_amount_usd} usdt, limit:{current_limit_down}".format(**locals()))

            #init usd buys
            #init sels

 
        # print(dir(net))
ow = Order_worker()
ow.init_net('')
