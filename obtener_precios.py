import yfinance as yf
import matplotlib.pyplot as plt
'''
def precios():
    tickets = ['BTC-USD','ETH-USD','BNB-USD']
    datos_cripto = {}
    for tick in tickets:
        datos = yf.Ticker(tick)
        datos_cripto[tick] = datos.info['currentPrice']
        return datos_cripto
    
'''

datos = yf.Ticker('BTC-USD')
#marker = datos.info["marketCap"]

precios = datos.history(period = "max")
#precios = datos.history(start = "2020-01-01", end = "2021-01-01")
print(precios)