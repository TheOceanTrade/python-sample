
from socketIO_client_nexus import SocketIO
import json

def on_connect():
    print('connect')

def on_message(message):
    print(message)

with SocketIO('https://dev-ws.theoceanx.com', 443) as socket:
    socket.emit('data', {
        'type': 'subscribe',
        'channel': 'order_book',
        'payload': {
          'baseTokenAddress': '0x6ff6c0ff1d68b964901f986d4c9fa3ac68346570',
          'quoteTokenAddress': '0xd0a1e359811322d97991e03f863a0c30c2cf029c',
          'snapshot': 'true',
          'depth': '100'
        }
    })
    socket.on('message', on_message)
    socket.on('connect', on_connect)
    socket.wait()
