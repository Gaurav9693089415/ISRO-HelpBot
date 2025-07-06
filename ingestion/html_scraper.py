import os
import requests
from bs4 import BeautifulSoup

BASE_URLS = [
    "https://www.mosdac.gov.in/",
    "https://www.mosdac.gov.in/faqs",
    "https://www.mosdac.gov.in/data",
    "https://www.mosdac.gov.in/productdetail"
]

OUTPUT_DIR = "data/html"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_html(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            filename = url.split("/")[-1] or "index"
            filepath = os.path.join(OUTPUT_DIR, f"{filename}.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(soup.prettify())
            print(f"✅ Saved: {filepath}")
        else:
            print(f"❌ Failed to fetch: {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"⚠️ Error for {url}: {str(e)}")

if __name__ == "__main__":
    for url in BASE_URLS:
        save_html(url)
