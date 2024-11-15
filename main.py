import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_URL = ' https://appbrewery.github.io/Zillow-Clone/'
GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/10IQt5UQ7E5J3Hn4uZWu3beKJV87idMBxYX7aG6pPRV8/edit'


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(ZILLOW_URL, headers=header).text

soup = BeautifulSoup(response, "html.parser")

# links to the property

links = []
all_links = soup.select(".StyledPropertyCardDataWrapper a")
for link_element in all_links:
    link = link_element["href"]
    links.append(link)

# address of the property

addresses = []
all_addresses = soup.select(".StyledPropertyCardDataWrapper address")
for address in all_addresses:
    edited_address = (address.text.replace("\n                                 ", "")
                      .replace("\n                                ", ""))
    addresses.append(edited_address)

# price of the property

prices = []
all_prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
for price in all_prices:
    edited_price = (price.text.replace("+/mo", "").replace("/mo", "")
                    .replace("+ 1 bd", ""))
    prices.append(edited_price)


# selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(GOOGLE_FORM_URL)

time.sleep(5)


for i in range(len(addresses)):

    q1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q1.send_keys(addresses[i])
    time.sleep(2)

    q2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q2.send_keys(prices[i])
    time.sleep(2)

    q3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q3.send_keys(links[i])
    time.sleep(2)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(5)

    another_response = driver.find_element(By.PARTIAL_LINK_TEXT, "Submit")
    another_response.click()
    time.sleep(5)
