# Data Entry Automation

This script automates scraping property data (address, price, and links) from a Zillow clone website and populates the data into a Google Form using Selenium.

---

## Features

1. **Web Scraping with BeautifulSoup**:
   - Scrapes property details such as address, price, and links from the provided Zillow clone URL.

2. **Automated Form Filling with Selenium**:
   - Populates a Google Form with the scraped data and submits it.

---

## Requirements

- **Python 3.7 or higher**
- **Google Chrome**
- **ChromeDriver** (matching your Chrome version)
- **Required Libraries**:
  - `bs4` (BeautifulSoup)
  - `requests`
  - `selenium`

Install the required libraries using:

    pip install beautifulsoup4 requests selenium

## Setup Instructions

### 1. Download ChromeDriver
- Ensure you have Google Chrome installed.  
- Download ChromeDriver that matches your Chrome version from:  
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

### 2. Update ChromeDriver Path
- Place ChromeDriver in a directory included in your system PATH.  
- Alternatively, update the explicit path in the script:

      driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)

### Update URLs

Replace the placeholders in the script with the actual URLs:

    ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
    GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/your-google-form-id/edit'

## Disclaimer
- This script is intended for educational purposes only.
- Use responsibly and comply with the terms and conditions of the websites involved.







