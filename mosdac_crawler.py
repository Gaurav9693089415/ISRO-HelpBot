# mosdac_crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

BASE_URL = "https://www.mosdac.gov.in"
visited = set()
max_pages = 30
output_dir = "data/mosdac_pages"
os.makedirs(output_dir, exist_ok=True)

# Track downloaded files
DOC_TYPES = [".pdf", ".docx", ".xlsx"]

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.netloc == urlparse(BASE_URL).netloc

def save_page_text(url, content, index):
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    filename = f"page_{index:02d}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\n\n{text}")
    return filename

def download_file(url, folder="data/mosdac_pages"):
    try:
        filename = os.path.basename(url.split("?")[0])
        filepath = os.path.join(folder, filename)

        if os.path.exists(filepath):
            print(f" Skipped (already exists): {filename}")
            return

        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f" Downloaded file: {filename}")
    except Exception as e:
        print(f" Failed to download {url}: {e}")


def crawl(url, depth=0):
    global visited
    if url in visited or len(visited) >= max_pages:
        return
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            visited.add(url)
            filename = save_page_text(url, response.text, len(visited))
            print(f"[+] Saved: {filename}")

            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if is_valid_url(full_url):
                    # Download files if they end with .pdf, .docx, .xlsx
                    if full_url.lower().endswith((".pdf", ".docx", ".xlsx")):
                        download_file(full_url)
                    else:
                        crawl(full_url, depth + 1)
    except Exception as e:
        print(f"[!] Failed to crawl {url}: {e}")


if __name__ == "__main__":
    crawl(BASE_URL)
