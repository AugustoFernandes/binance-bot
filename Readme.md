# BINANCE BOT
## Как начать
`$ python3 webAdmin.py` - запуск веб-админки
`$ python3 worker.py` - начало торговли

## Account settings section
`API_URL = "https://api.binance.com/"`  
`API_KEY = "Q9uXG8pOjkmwhes2roxREu0UMEcAcIRkZpZbDIYnfkWXvlETAYH9rYrZSasUsal5"`  
`API_SECRET = "uiU8vZAGJVAjvMoDjAP3hOAiKEKeYk1ARUzqtAH5tRa6dCjDf4f07bkVhNzgtDcJ"`    
`smbl = "BTCUSDT"`  

### `API_URL` - ссылка для обращения к Binance API
### `API_KEY` - публичный ключ API
### `API_SECRET` - секретный ключ API, используется для подписи приватных методов обращения к API
### `smbl` - symbol или валютная пара, если нужно изменить валютную пару - измените значение. Строка должна быть в верхнем регистре, при обращении к WebSocket API форматирование в нижний регистр учтено

## Worket.py settings
`settings = {'rate': 5000, 'amount_btc': 1, 'amount_usd': 100}`  
`rate` - релевантная цена на криптовалюту  
`amoun_btc` - ваше количество btc 
`amount_usd` - ваше количество usd 

## Basic methods

### Web Socket API call    
`getSockStream()` - функция обращения к Web Socket API для получения информации о валютной паре в реальном времени. Подключение к Web Socket API должно быть активным не более 24 часов во избежание бана IP-адреса  
#### Response:   
`{`  
      `"e": "aggTrade",  // Тип события`  
      `"E": 123456789,   // Время отправки события`  
      `"s": "BNBBTC",    // Пара`  
      `"a": 12345,       // ID возвращаемой записи`  
      `"p": "0.001",     // Цена`  
      `"q": "100",       // Кол-во`  
      `"f": 100,         // ID первой сделки`  
      `"l": 105,         // ID последней сделки`  
      `"T": 123456785,   // Время сделки`  
      `"m": true,        // Покупатель мейкер?`    
      `"M": true         // Не актуально.`  
`}`  

<hr>

### Create Order
 `bot.testOrder(...)` - тестовый ордер, в случае правильной настройки передаваемых параметров возвращает пустой словарь `{}`  
 `bot.createOrder(...)` - создать оредр, передаваемые параметры идентичны с `bot.testOrder(...)`
#### Request:
`bot.testOrder(`  
      `symbol = smbl,        # Валютная пара (см. настройки)`  
      `recvWindow = 5000,    # Настройка из доки, выставлена по умолчанию`  
      `side = 'BUY',         # Тип ордера (BUY OR SELL)`  
      `type = 'LIMIT',       # Тип оредра из доки апишки`  
      `timeInForce = 'GTC',  # GTC (Good Till Cancelled)  - ордер активен пока его не отменят`  
      `quantity = 1,         # Количество покупки`  
      `price = 5600,         # Цена`  
`)`   
#### Respone:
 `{`  
      `"symbol": "BTCUSDT",`  
      `"orderId": 28,`  
      `"clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",`  
      `"transactTime": 1507725176595,`  
      `"price": "0.00000000",`  
      `"origQty": "10.00000000",`  
      `"executedQty": "10.00000000",`  
      `"status": "FILLED",`  
      `"timeInForce": "GTC",`  
      `"type": "MARKET",`  
      `"side": "SELL",`  
      `"fills": [`  
        `{`  
          `"price": "4000.00000000",`  
          `"qty": "1.00000000",`  
          `"commission": "4.00000000",`  
          `"commissionAsset": "USDT"`  
        `},`  
        `{`  
          `"price": "3999.00000000",`  
          `"qty": "5.00000000",`  
          `"commission": "19.99500000",`  
          `"commissionAsset": "USDT"`  
        `},`  
        `{`  
          `"price": "3998.00000000",`  
          `"qty": "2.00000000",`  
          `"commission": "7.99600000",`  
          `"commissionAsset": "USDT"`  
        `},`  
        `{`  
          `"price": "3997.00000000",`  
          `"qty": "1.00000000",`  
          `"commission": "3.99700000",`  
          `"commissionAsset": "USDT"`  
        `},`  
        `{`  
          `"price": "3995.00000000",`  
          `"qty": "1.00000000",`  
          `"commission": "3.99500000",`  
          `"commissionAsset": "USDT"`  
        `}`  
    `]`  
`}`    

> `type` - тип ордера  
> В зависимости от типа ордера, некоторые параметры становятся обязательными:  
>>   Тип ордера — Обязательные параметры  
>>   LIMIT — timeInForce, quantity, price  
>>   MARKET — quantity  
>>   STOP_LOSS — quantity, stopPrice  
>>   STOP_LOSS_LIMIT — timeInForce, quantity, price, stopPrice  
>>   TAKE_PROFIT — quantity, stopPrice  
>>   TAKE_PROFIT_LIMIT — timeInForce, quantity, price, stopPrice  
>>   LIMIT_MAKER — quantity, price  

> Ордера типа LIMIT_MAKER – это ордера типа обычного LIMIT, но они отклонятся, если ордер при выставлении может выполниться по рынку. Другими словами, вы никогда не будете тейкером, ордер либо выставится выше/ниже рынка, либо не выставится вовсе.
> Ордера типа STOP_LOSS и TAKE_PROFIT исполнятся по рынку (ордер типа MARKET), как только будет достигнута цена stopPrice.
> Любые ордера LIMIT или LIMIT_MAKER могут формировать ордер-айсберг, установив параметр icebergQty.
> Если установлен параметр icebergQty, то параметр timeInForce ОБЯЗАТЕЛЬНО должен иметь значение GTC.
> Для того, что бы выставлять цены, противоположные текущим для ордеров типов MARKET и LIMIT:  
> Цена выше рыночной: STOP_LOSS BUY, TAKE_PROFIT SELL  
> Цена ниже рыночной: STOP_LOSS SELL, TAKE_PROFIT BUY  

<hr>  

### Delete Order
 `bot.cancelOrder(orderId = ..., symbol = smbl)` - отмена выставленного ордера, передает обязательный параметр orderId (integer) и валютную пару
 
<hr>
 
### Open Orders 
 `bot.openOrders()` - вовзращает список всех выставленных ордеров по всем валютным парам. Если передать параметр `smbl` `bot.openOrders(symbol=smbl)` - вернет список выставленных оредров по указанной валютной паре

<hr>
 
### Trades History
 `bot.myTrades(symbol = smbl)` - возвращает историю сделок пользователя
 
<hr> 
 
### Account Information
 `bot.account()` - возвращает информацию об аккаунте. Балансы в массиве `"balances": [{...}, {...}, {...}]`
 
#### Response:
`{`  
  `"makerCommission": 15,`  
  `"takerCommission": 15,`  
  `"buyerCommission": 0,`  
  `"sellerCommission": 0,`  
  `"canTrade": true,`  
  `"canWithdraw": true,`  
  `"canDeposit": true,`  
  `"updateTime": 123456789,`  
  `"balances": [`  
    `{`  
      `"asset": "BTC",`  
      `"free": "4723846.89208129",`  
      `"locked": "0.00000000"`  
    `},`  
    `{`       
      `"asset": "LTC",`  
      `"free": "4763368.68006011",`  
      `"locked": "0.00000000"`  
    `}`  
  `]`  
`}`  


# Administrator web interface guide:

## Settings(index page):  
1) Введите данные в поля `API_KEY`, `API_SECRET` и `symbol`(ex. BTCUSDT) и нажмите save чтобы сохранить настройки в файл бота  
2) Если вы хотите поменять ключи, в файле index.py удалите строчки `12, 13, 14` и всегда оставляйте `11` строку пустой, и повторите пункт 1   
  
## Orders net:  
Заполните таблицу и нажмите `create` чтобы сохранить данные   
Чтобы создать новую сетку - в файле start_net.py удалите список после `return` и приведите к виду  
`def get_start_net():`  
`   return           `  
`                    `  
строка `3` должна оставаться пустой 
