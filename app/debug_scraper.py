from playwright.sync_api import sync_playwright
from urllib.parse import urlparse
from datetime import datetime
import os
import time
import random
# Assuming get_filename and sanitize_title are part of scraper.py
from scraper import sanitize_title

def capture_console(msg):
    print(f"CONSOLE LOG: {msg.text}")

def get_debug_filename(url, suffix):
    """
    Generates a filename for debugging purposes, including sanitized title and timestamp.
    Adjusted to generate filenames for screenshot and HTML content.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2] if len(parsed_url.netloc.split('.')) > 2 else parsed_url.netloc
    path = parsed_url.path.replace('/', '_') if parsed_url.path else "homepage"
    sanitized_path = sanitize_title(path)
    timestamp = datetime.now().strftime('%Y-%m-%d_T%H%M%S')
    filename = f"{domain}.{sanitized_path}.{timestamp}{suffix}"
    return filename

def debug_scrape(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        ]
        context = browser.new_context(user_agent=random.choice(user_agents))
        
        page = context.new_page()
        page.on("console", capture_console)
        
        print(f"Navigating to {url}")
        delay = random.uniform(2, 5)
        time.sleep(delay)
        response = page.goto(url, wait_until="networkidle")
        print(f"Navigation response status: {response.status}")
        
        post_navigation_delay = random.uniform(1, 3)
        time.sleep(post_navigation_delay)
        
        # Directory for debug files
        debug_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "debug")
        os.makedirs(debug_dir, exist_ok=True)
        
        # Generate filenames for screenshot and HTML content
        screenshot_filename = get_debug_filename(url, "_screenshot.png")
        html_filename = get_debug_filename(url, "_content.html")
        
        screenshot_path = os.path.join(debug_dir, screenshot_filename)
        html_path = os.path.join(debug_dir, html_filename)
        
        # Take a screenshot and save HTML content
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
        content = page.content()
        with open(html_path, 'w') as f:
            f.write(content)
        print(f"Page HTML content saved to {html_path}")
        
        browser.close()

if __name__ == "__main__":
    url = input("Enter the URL of the product documentation or guide: ")
    debug_scrape(url)
