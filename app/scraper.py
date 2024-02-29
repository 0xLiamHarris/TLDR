import json
import requests
import time
import random
import os
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise HTTPError for bad requests (400+)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup, None
    except requests.RequestException as e:
        return None, str(e)

def scrape_with_playwright(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)  # Change to False if debugging
            
            # Randomize User-Agent
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            ]
            context = browser.new_context(user_agent=random.choice(user_agents))
            
            page = context.new_page()
            
            # Random delay to mimic human behavior
            delay = random.uniform(2, 5)
            time.sleep(delay)
            
            page.goto(url, wait_until='networkidle')
            
            time.sleep(random.uniform(1, 3))
            
            content = page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            browser.close()
            return soup, None
    except Exception as e:
        return None, str(e)

def sanitize_title(title):
    invalid_chars = ':|?*"<>\\/'
    sanitized = ''.join('_' if c in invalid_chars else c for c in title).strip()[:50]
    return sanitized

def get_filename(url, title):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2] if len(parsed_url.netloc.split('.')) > 2 else parsed_url.netloc
    sanitized_title = sanitize_title(title)
    timestamp = datetime.now().strftime('%Y-%m-%d_T%H%M%S')
    filename = f"{domain}.{sanitized_title}.{timestamp}.json"
    return os.path.join('output', filename)

def save_to_json(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def clean_content(content):
    seen = set()
    cleaned_content = []
    for item in content:
        # Create a unique identifier for each item based on its tag and text
        identifier = f"{item['tag']}_{item['text']}"
        if item['text'] and identifier not in seen:
            seen.add(identifier)
            cleaned_content.append(item)
    return cleaned_content

def main():
    url = input("Enter the URL of the product documentation or guide: ")
    soup, error = scrape_url(url)
    
    if not soup:
        print(f"Failed to fetch content using requests: {error}. Trying with Playwright...")
        soup, error = scrape_with_playwright(url)
        if not soup:
            print(f"Failed to fetch content using Playwright: {error}. Exiting...")
            return
    
    title = soup.title.string if soup.title else 'No Title Found'
    tags = ['h1', 'h2', 'h3', 'p', 'pre', 'code', 'span', 'div', 'section']
    raw_content = [{'tag': el.name, 'text': el.get_text(strip=True)} for el in soup.find_all(tags)]
    
    # Clean the content before saving
    content = clean_content(raw_content)
    
    filename = get_filename(url, title)
    save_to_json(content, filename)
    
    print(f"Content successfully scraped and saved to {filename}")

if __name__ == "__main__":
    main()
