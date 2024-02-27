# TLDR App

## Overview

TLDR is a Python application for scraping product documentation or guides from specified URLs, extracting relevant information, and saving it in a JSON format optimized for training GPT-4 models. It utilizes BeautifulSoup for static content and Playwright as a fallback for dynamic content that requires JavaScript execution.

## Installation

### Using `setup.py` (Recommended for most users)

This method installs TLDR and automatically sets up Playwright, including necessary browser binaries.

1. Clone this repository.
2. Navigate to the root directory of the cloned repository.
3. Create a virtual environment (optional but recommended):
   - `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install the package, which includes automatic Playwright setup:
   - `pip install .`

### For Development

If you're setting up TLDR for development purposes, follow these steps:

1. Clone this repository.
2. Navigate to the root directory of the cloned repository.
3. Create a virtual environment:
   - `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install the development requirements:
   - `pip install -r requirements.txt`
6. Manually install Playwright browsers:
   - `playwright install`

## Usage

After installation, you can run the application directly from the command line anywhere in your system by typing:
`TLDR`

Follow the on-screen prompts to enter the URL of the product documentation or guide you wish to scrape. The output will be saved in the `output` directory within the project folder, using a filename based on the domain and the time of scraping.

## Troubleshooting

In case you encounter any issues during the installation or running of TLDR, especially related to Playwright, consider manually running the Playwright installation command:
- `playwright install`

Ensure you have an active internet connection and necessary permissions for installation.

Should you encounter issues where TLDR fails to scrape content as expected, particularly with websites heavily reliant on JavaScript, the `debug_scraper` tool can be utilized for diagnostic purposes.

### Using `debug_scraper`

The `debug_scraper` tool is designed to emulate more closely human interactions with a webpage and can provide additional insights into why scraping might be failing. It captures screenshots and the HTML content of the page at the time of scraping, which can be helpful for identifying issues like JavaScript-rendered content not loading as expected.

To use `debug_scraper`, follow these steps:

1. Navigate to the `TLDR/app` directory within your project folder.
2. Run the `debug_scraper.py` script directly with Python:
   - `python debug_scraper.py`
3. When prompted, enter the URL of the page you're having trouble scraping.
4. The script will attempt to navigate to the page, waiting for network activities to idle, and then save both a screenshot and the HTML content to the `debug` folder within the main directory. The files are named using the domain, sanitized title, and a timestamp for easy identification.

### Reviewing Debug Output

After running `debug_scraper`, check the `debug` folder for the screenshot (`_screenshot.png`) and HTML (`_content.html`) files. These files can provide valuable insights:

- **Screenshot**: Helps in visually confirming what content was loaded on the page at the time of scraping. Useful for checking if essential elements are missing or if there are visible error messages.
- **HTML Content**: Allows for a detailed inspection of the page's HTML structure post-JavaScript execution. This can be critical for understanding how content is dynamically loaded and identifying the selectors needed for successful scraping.

If the content you're expecting is missing or if the page shows error messages, it might indicate issues such as the need for specific headers, cookies, or dealing with CAPTCHAs that require more advanced handling within the `scraper.py` or necessitate manual intervention.

Hit me up for further assistance or if the problem persists.
