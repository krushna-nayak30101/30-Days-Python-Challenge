import requests
from bs4 import BeautifulSoup

# URL for The Hindu's homepage
url = 'https://www.thehindu.com/'

# Send GET request
response = requests.get(url)

# Check response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find headlines from h3 or h2 tags (varies slightly)
    headlines = soup.find_all(['h3', 'h2'], class_='title')

    print("\n📰 The Hindu - Top Headlines:\n")
    for i, headline in enumerate(headlines[:10], 1):  # Show only top 10
        print(f"{i}. {headline.get_text(strip=True)}")
else:
    print("❌ Failed to fetch The Hindu homepage.")
