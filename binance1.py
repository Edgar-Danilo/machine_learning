from binance.spot import Spot
from datetime import datetime, timezone, timedelta
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

client = Spot()

datos = client.klines("BTCUSDT", "1m", limit=50)
# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos, columns=[
    'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 
    'Close Time', 'Quote Asset Volume', 'Number of Trades', 
    'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
])

print(datos)

# Suponiendo que df ya está definido y contiene datos de velas
# Calcular medias móviles
df['SMA_20'] = df['Close'].rolling(window=20).mean()  # Media Móvil Simple de 20 períodos
df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()  # Media Móvil Exponencial de 20 períodos

# Graficar
apds = [
    mpf.make_addplot(df['SMA_20'], color='blue', title='SMA 20'),
    mpf.make_addplot(df['EMA_20'], color='red', title='EMA 20')
]


# Convertir el tiempo de apertura a un formato legible
df['Open Time'] = pd.to_datetime(df['Open Time'])
df.set_index('Open Time', inplace=True)

df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')


mpf.plot(df, type='candle', style='charles', ylabel='Price', volume=True, addplot=apds)
#plt.show()

'''
for i in datos:
    # Convertir a segundos
    timestamp_s = i[0] / 1000

    # Convertir a objeto datetime en UTC
    fecha_utc = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)
    # Restar 5 horas usando timedelta
    fecha = fecha_utc - timedelta(hours=5)
    print("Date: ",fecha,"Open: ",i[1],"High: ",i[2], "Low: ",i[3],"Close: ",i[4])
'''
