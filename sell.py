import ccxt
with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()
binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret
})

import requests
def post_message(token, channel, text):
    response=requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
myToken = "xoxb-1610685610342-2019607257925-wq5VcryqFQKyhdEQwuuj6voz"

print("hello comrades")
balance = 0
day = 1
daycri = 1
usdtava = 0
usdtava0 = 0
bnb = ccxt.binance()

usdtmar = []
usdtmarus = []
pricecri3 = []
tracking = []
pricemax = []
trial = 0
trialstack = 0

import time
import datetime
while True:
    now = datetime.datetime.now()
    nowhour = now.hour
    nowminute = now.minute
    nowday = str(now.year) +'y'+ str(now.month) +'m'+ str(now.day) +'d'
    nowtime = str(now.hour) +'h'+ str(now.minute) +'m'+ str(now.second) +'s'

    if nowhour == 0 and nowminute == 0 and day == daycri:
        usdtmar = []
        usdtmarus = []
        pricecri3 = []
        tracking = []
        pricemax = []
        trial = 0
        trialstack = 0

        markets = bnb.load_markets()
        markeys = list(markets.keys())
        print(markeys)
        lenmar = len(markeys)

        for a in markeys:
            if a[-4:] == 'USDT':
                usdtmarus.append(a)

        for c in usdtmarus:
            e = c[:-5]
            usdtmar.append(e)

        post_message(myToken, "#project-neo", "Comrades, " + nowday + " today is "
                     + day + "th day after first trade.\n"
                     + "I wish you success the revolution.")

        for f in usdtmarus:
            ohlcv = bnb.fetch_ohlcv(f)
            pricecri1 = ohlcv[0][-1]
            pricecri2 = pricecri1 * 1.2
            pricecri3.append(pricecri2)

        day+=1

    elif nowhour == 23 and nowminute == 59 and day!=daycri:
        newbalance = binance.fetch_balance()
        usdt = newbalance['USDT']['free']
        bal1 = usdt - balance
        bal2 = str(round(bal1,2))
        bal3 = bal1/balance*100
        bal4 = str(round(bal3,2))
        post_message(myToken, "#project-neo", "Comrades, " + nowday + " trade is over.\n"
                     + "Today " + bal2 + " USD received and earning rate is " + bal4 + "%.")
        balance = usdt
        usdtava0 = usdt / 5
        usdtava = round(usdtava0,2)
        daycri+=1

    else:
        for h in range(0,len(usdtmar)):
            i = usdtmarus[h]
            j = usdtmar[h]
            pricenow1 = bnb.fetch_ticker(i)
            pricenow2_br = pricenow1['close']
            pricenow2 = round(pricenow2_br,4)
            pricecri4 = pricecri3[h]
            if pricenow2 > pricecri4 and trial < 5:
                amount0 = usdtava0/pricenow2
                amount1 = round(amount0,4)
                buy = binance.create_market_buy_order(i, amount1)
                trial+=1
                trialstack+=1
                timecri1 = time.time()
                post_message(myToken,"#project-neo","Comrades, "+nowday+nowtime+"\nToday's "
                            +trialstack+"th buy is completed.\nOne"
                            +j+" per "+str(pricenow2)+"dollar "+str(usdtava)+"dollar amount bought.")
                tracking.append([j,i,amount0])
                pricemax.append(pricenow2)
                del usdtmarus[h]
                del usdtmar[h]

        for k in range(0,len(tracking)):
            l = tracking[k]
            pricenow3 = bnb.fetch_ticker(k)
            pricenow4_br = pricenow3['close']
            pricenow4 = round(pricenow4_br,4)
            if pricemax[k] < pricenow4:
                del pricemax [k]
                pricemax.insert(k,pricenow4)
            pricecri5 = pricemax*0.8+pricenow2*0.2
            timecri2 = time.time()
            timecri3 = timecri2 - timecri1
            if pricenow4 < pricecri5 and timecri3 > 600:
                amount2 = tracking[k][2]
                m = tracking[k][0]
                n = tracking[k][1]
                sell1 = binance.create_market_sell_order(n,amount2)
                trial-=1
                trialminus = trialstack - trial
                post_message(myToken,"#project-neo","Comrades, "+nowday+nowtime+"\nToday's "
                            +str(trialminus)+"th sell is completed.\nOne"
                            +m+" per "+str(pricenow4)+"dollar all sold.")

            o = tracking[k]
            pricenow5 = bnb.fetch_ticker(o)
            pricenow6_br = pricenow5['close']
            pricenow6 = round(pricenow6_br,4)
            pricecri6 = pricenow2*0.9
            timecri4 = time.time()
            timecri5 = timecri4 - timecri1
            if pricenow6 < pricecri6 and timecri5 > 10:
                amount3 = tracking[k][2]
                p = tracking[k][0]
                q = tracking[k][1]
                sell2 = binance.create_market_sell_order(q,amount3)
                trial-=1
                trialminus = trialstack - trial
                post_message(myToken,"#project-neo","Comrades, "+nowday+nowtime+"\nToday's "
                            +trialminus+"th sell is completed.\nOne"
                            +p+" per "+str(pricenow6)+"dollar all sold.")
        time.sleep(89)
        print("no error")