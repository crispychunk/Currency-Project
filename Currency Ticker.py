import json
import requests 
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import pandas as pd
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
import time as t
import matplotlib
from tkinter import *
import threading
from multiprocessing import Pool
def getData():
    headers = {'Authorization': 'Bearer 1040f3b6997e1c6db66f7bb3bb8b5336-4ec7a67d82e48258fe56ac32c283eb12'}

    response = requests.get('https://api-fxpractice.oanda.com/v3/accounts', headers=headers)
    if response.status_code == 200:
        print("Authentication successful")
    return response
def getPrice(ticker_type):
    
    
    accountID = "101-002-12644151-001"
    api = API(access_token="1040f3b6997e1c6db66f7bb3bb8b5336-4ec7a67d82e48258fe56ac32c283eb12")
    params ={"instruments": ticker_type}
    print(ticker_type)
    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)
    
    
    data = pd.DataFrame(r.response["prices"])
    data_text = json.dumps(r.response, indent=2)
    ask = str(data["asks"])
    bid = str(data["bids"])
    #print(data_text) Update ** Allow it to be display different amount of digits properly
    bid_price = ""
    ask_price = ""
    for ch in range( 4,len(ask)):
        if (ask[ch].isdigit() or ask[ch] == ".") and ch < 24:
            ask_price += ask[ch]
            bid_price += bid[ch]

    print("ASK:" + ask_price)
    print("BID:" + bid_price)
    print("#######################")
    return ask_price,bid_price
def accountInfo():
    # get a list of trades
    from oandapyV20 import API
    import oandapyV20.endpoints.trades as trades

    api = API(access_token="1040f3b6997e1c6db66f7bb3bb8b5336-4ec7a67d82e48258fe56ac32c283eb12")
    accountID = "101-002-12644151-001"

    r = trades.TradesList(accountID)
    # show the endpoint as it is constructed for this call
    print("REQUEST:{}".format(r))
    rv = api.request(r)
    print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))
def Main():
    ticker= ""
    getPrice(ticker)
    getData()


def gui():
    
    #####################
    root = Tk()
    topWidget = Frame(root)
    topWidget.pack()
    
    # Button creator
    bottomWidget = Frame(root)
    bottomWidget.pack(side=BOTTOM)
    title =Label(topWidget, text = "Currency Converter", fg = "Black",font=("Courier", 20))
    title.pack()
    ###############
    option = ["AUD_CAD", "AUD_CHF", "AUD_HKD", "AUD_JPY", "AUD_NZD", "AUD_SGD", "AUD_USD", "CAD_CHF", "CAD_HKD",
              'CAD_JPY', "CAD_SGD", "CHF_HKD", "CHF_JPY", "CHF_ZAR", "EUR_AUD", "EUR_CAD", "EUR_CHF", "EUR_CZK",
              "EUR_DKK", "EUR_GBP", "EUR_HKD", "EUR_HUF", "EUR_JPY", "EUR_NOK", "EUR_NZD", "EUR_PLN", "EUR_SEK",
              "EUR_SGD", "EUR_TRY", "EUR_USD", "EUR_ZAR", "GBP_AUD", "GBP_CAD", "GBP_CHF", "GBP_HKD", "GBP_JPY",
              "GBP_NZD", "GBP_PLN", "GBP_SGD", "GBP_USD", "GBP_ZAR", "HKD_JPY", "NZD_CAD", "NZD_CHF", "NZD_HKD",
              "NZD_JPY", "NZD_SGD", "NZD_USD", "SGD_JPY", "TRY_JPY", "USD_CAD", "USD_CHF", "USD_CNH", "USD_CZK",
              "USD_DKK", "USD_HKD", "USD_HUF", "USD_INR", "USD_JPY", "USD_MXN", "USD_NOK", "USD_PLN", "USD_SAR",
              "USD_SEK", "USD_SGD", "USD_TBH", "USD_TRY", "USD_ZAR", "ZAR_JPY"]
    variable = StringVar(topWidget)
    variable.set(option[0])
    ticker = OptionMenu(topWidget, variable, *option)
       
    ticker.pack()
    ################
    def tickerType():
        ticker_type = variable.get()

        askLabel.config(text=getPrice(ticker_type))
    buttonTest = Button(bottomWidget, text="Get price", fg="Black", command=tickerType)
    buttonTest.pack()
    ############################################
    ticker_type = variable.get()
    ticker_Identifier = Label(topWidget, text="Ask:     Bid:", width=20, font=("Courier", 30))
    ticker_Identifier.pack(side= TOP)

    askLabel = Label(bottomWidget, text= "-------------",width=20, font=("Courier", 30),bg = "Grey" )
    askLabel.pack(side= BOTTOM)
    def askTicker(ticker_type):
        askLabel.config(text=getPrice(ticker_type))








    #th = threading.Thread( target=askTicker, args =[ticker_type])
    #th.start()
    #th.join()


    root.mainloop()
gui()
