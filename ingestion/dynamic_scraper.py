import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

OUTPUT_DIR = "data/html"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Setup headless Chrome
def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)

def save_dynamic_page(url, filename):
    driver = get_driver()
    try:
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load
        page_html = driver.page_source
        file_path = os.path.join(OUTPUT_DIR, f"{filename}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f" Saved dynamic page: {file_path}")
    except Exception as e:
        print(f" Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    dynamic_pages = {
        "https://www.mosdac.gov.in/liveMap": "live_map",
        "https://www.mosdac.gov.in/satProducts": "satellite_products"
    }

    for url, fname in dynamic_pages.items():
        save_dynamic_page(url, fname)
