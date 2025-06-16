# 🎯 Topic: 
-  🔹 Sockets .
-  🔹 HTTP Requests

Challennge -  Write a Python script to fetch and display live content from a webpage using the requests library.

I chose to pull product info from a public test API (fakestoreapi.com) — simulating how a retail app fetches product listings in real time.

**✅ Use socket to send a product ID from POS to the inventory system**
**✅ Use requests to fetch live product details from an API (fakestoreapi.com)**

**🔁 Workflow Simulation:
🧾 POS system sends product ID to inventory server (via socket)

🌐 Inventory server receives the ID and fetches product name + price using HTTPS

📦 Server prints complete product info — like a real-time lookup!
**
 🧵 What I did:
### Client Pos

 
```
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
````

### Server inventory
```

import socket

client = socket.socket()
client.connect(('localhost', 9090))

# Just sending product ID — the server will fetch full info
product_id = "2"
client.send(product_id.encode('utf-8'))

print("✅ POS sent product ID:", product_id)
client.close()
```

💡 Quick Tip:
Use sockets when you want fast, internal app-to-app communication

Use HTTP(S) when fetching resources from web services or APIs 

📚 Key Learning:
In modern retail tech, it’s not just about writing code — it’s about making systems talk in real time and sync up across local and web platforms.
Python makes this orchestration incredibly clean and powerful.

#Day20 #30DaysOfPython #SocketProgramming #HTTPSRequests #RetailTech #PythonProjects #KrushnaCodes #APIs #PythonNetworking
