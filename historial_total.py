from binance.spot import Spot
import pandas as pd
from datetime import datetime, timedelta,timezone
import time

client = Spot()

# Función para obtener datos de velas en un rango de tiempo
def obtener_datos_klines(symbol, interval, start_time, end_time):
    datos = []
    while start_time < end_time:
        response = client.klines(symbol, interval, startTime=start_time, endTime=end_time, limit=1000)
        if not response:
            break
        datos.extend(response)
        # Actualizar start_time para la próxima solicitud
        start_time = response[-1][0] + 1
        # Evitar superar los límites de la API
        time.sleep(1)
    return datos

# Fecha de inicio y fin
fecha_inicio = datetime(2017, 8, 17)  # Fecha en la que BTC/USDT comenzó a cotizar
fecha_actual = datetime.now(timezone.utc)  # Fecha actual en UTC

# Convertir fechas a timestamps
start_time = int(fecha_inicio.timestamp() * 1000)
end_time = int(fecha_actual.timestamp() * 1000)

# Obtener todos los datos de velas
datos = obtener_datos_klines("BTCUSDT", "1d", start_time, end_time)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos, columns=[
    'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 
    'Close Time', 'Quote Asset Volume', 'Number of Trades', 
    'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
])

# Convertir el tiempo de apertura a un formato legible
df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
df.set_index('Open Time', inplace=True)

# Convertir columnas a tipo numérico
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
df['Quote Asset Volume'] = pd.to_numeric(df['Quote Asset Volume'], errors='coerce')
df['Taker Buy Base Asset Volume'] = pd.to_numeric(df['Taker Buy Base Asset Volume'], errors='coerce')
df['Taker Buy Quote Asset Volume'] = pd.to_numeric(df['Taker Buy Quote Asset Volume'], errors='coerce')
df['Ignore'] = pd.to_numeric(df['Ignore'], errors='coerce')

# Guardar el DataFrame en un archivo CSV (opcional)
df.to_csv('btcusdt_1d.csv', index=True)

print(f"Se han obtenido {len(df)} velas de 1 minuto.")
