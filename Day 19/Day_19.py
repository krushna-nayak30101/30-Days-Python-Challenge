import threading, requests, time

# Simulated retail files (catalogs, images, reports)
urls = [
    "https://file-examples.com/storage/fe40fe647dc7d4600cd0bb7/2017/10/file-sample_150kB.pdf",        # Retail catalog
    "https://file-examples.com/storage/fe40fe647dc7d4600cd0bb7/2017/10/file_example_JPG_100kB.jpg",   # Product image
    "https://file-examples.com/storage/fe40fe647dc7d4600cd0bb7/2017/02/file-sample_100kB.doc"         # Price report
]

def download(url):
    filename = url.split("/")[-1]
    try:
        print(f"📦 Downloading: {filename}")
        with open(filename, "wb") as file:
            file.write(requests.get(url).content)
        print(f"✅ Completed: {filename}")
    except Exception as e:
        print(f"❌ Failed: {filename} ({e})")

start = time.time()
threads = [threading.Thread(target=download, args=(u,)) for u in urls]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
print(f"\n⏱️ All downloads finished in {time.time() - start:.2f} seconds.")
