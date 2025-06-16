import socket

client = socket.socket()
client.connect(('localhost', 9090))

# Just sending product ID — the server will fetch full info
product_id = "2"
client.send(product_id.encode('utf-8'))

print("✅ POS sent product ID:", product_id)
client.close()
