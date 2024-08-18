import websocket,json,pprint

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

def open(ws):
    print("Conexion abierta")

def close(ws):
    print("Conexion cerrada")

def mensaje(ws,massage):
    #print(massage)
    json_mensaje = json.loads(massage)
    pprint.pprint(json_mensaje)
    print("Conexion abierta")

ws = websocket.WebSocketApp(SOCKET, on_open = open, on_close = close, on_message = mensaje)
ws.run_forever()
