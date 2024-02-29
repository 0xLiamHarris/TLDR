# TLDR

## Overview

TLDR is a Python app specifically geared for scraping product documentation or guides from specified URLs, extracting relevant information, and saving it to LLM-optimized JSON for training models. It utilizes [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for static content and [Playwright](https://playwright.dev/) as a fallback for dynamic content that requires JavaScript execution.

TL;DR: app scrapey; GPT thinky

## On Deck
- Better DOM preprocessing
- LLM handles data transformation
- Making it cool and good
- Mapping & aggregating data would also be cool

## Installation

### Prerequisites
Python 3.8 or higher.

### General Installation (Recommended)

This method installs **TLDR** and all associated dependencies.

1. Clone this repository.
2. Navigate to the root directory of the cloned repo.
3. Create a virtual environment *(optional but recommended)*:
   - **Windows**: `python -m venv venv` then `venv\Scripts\activate`
   - **Unix/MacOS**: `python3 -m venv venv` then `source venv/bin/activate`
4. Install TLDR with dependencies:
   - Run `pip install .`
   - The post-installation script attempts to install Playwright browsers automatically.

### For Development

If you're setting up **TLDR** for dev/debugging or need manual control over the installation process, follow these steps:

1. Follow steps 1 to 3 as outlined in General Installation.
2. Install development dependencies:
   - `pip install -r requirements.txt`
3. Manually install Playwright:
   - `playwright install`

## Usage

After installation, you can run **TLDR** directly from the command line anywhere in your system by typing:
`TLDR`

Follow the on-screen prompts to enter the URL of the product documentation or guide you wish to scrape. The output will be saved in the `output` directory within the project folder, using a filename based on the domain and the time of scraping.

## Troubleshooting

In case you encounter any issues during the installation or running of TLDR, especially related to Playwright, consider manually running the Playwright installation command:
- `playwright install`

Should you encounter issues where TLDR fails to scrape content as expected, particularly with websites heavily reliant on JavaScript, the `debug_scraper` tool can be utilized for diagnostic purposes.

## Using `debug_scraper`

The `debug_scraper` tool is designed to emulate more closely human interactions with a webpage and can provide additional insights into why scraping might be failing. It captures screenshots and the HTML content of the page to `~/output` at the time of scraping.

This can be helpful for identifying issues like JavaScript-rendered content not loading as expected.

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

## License

TLDR is released under the MIT License. Check the LICENSE file in the project root for more info.