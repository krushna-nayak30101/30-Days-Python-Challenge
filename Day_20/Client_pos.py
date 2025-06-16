import socket
import requests

server = socket.socket()
server.bind(('localhost', 9090))
server.listen(1)

print("🟢 Inventory server is running... Waiting for POS system.")

conn, addr = server.accept()
print("✅ Connected by:", addr)

product_id = conn.recv(1024).decode('utf-8')
print(f"📥 Received Product ID from POS: {product_id}")

# Fetch product info from online API using HTTPS
url = f"https://fakestoreapi.com/products/{product_id}"
response = requests.get(url)

if response.ok:
    product = response.json()
    print("📦 Product Info Fetched:")
    print("🛍️ Title:", product['title'])
    print("💰 Price: ₹", product['price'])
else:
    print("❌ Failed to fetch product details.")

conn.close()
