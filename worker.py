# Импортим сетку и бота+валютную пару
from start_net import get_start_net 
from index import bot, smbl
import math

# Тут я превожу значения в сетке в float 
# потому что из админке в start_net они в str передаются
start_net = get_start_net()
for sub in start_net:
    for key in sub:
        sub[key] = float(sub[key])

# Настройки
settings={'rate': 7001, 'amount_btc': 1, 'amount_usd': 100}
rate = settings['rate']
amount_btc = settings['amount_btc']
amount_usd = settings['amount_usd']
current_limit_down = rate
current_limit_up = rate

# запускаем торговлю
for step in start_net:
    current_limit_up = current_limit_up + float(rate)*step['step']
    current_limit_down = current_limit_down + float(rate)*step['step']
    if step['amount'] == 0:
            continue
    current_amount_btc = amount_btc*step['amount']
    current_amount_usd = amount_usd*step['amount']
    print("[*] BUY ORDER for %s"%smbl, bot.testOrder(
            symbol = smbl,        
            recvWindow = 5000,    
            side = 'BUY',         
            type = 'LIMIT',       
            timeInForce = 'GTC',  
            quantity = current_amount_btc,
            price = round(current_limit_down, 4),
        ))
    print("[*] SELL ORDER FOR %s"%smbl, bot.testOrder(
            symbol=smbl,
            recvWindow=5000,
            side='SELL',
            type='LIMIT',
            timeInForce='GTC',
            quantity=current_amount_usd,
            price=round(current_limit_up, 4)
        ))   
