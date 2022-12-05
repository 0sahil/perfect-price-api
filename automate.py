from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# connect to google.com
driver = webdriver.Chrome(options=Options())
driver.get("https://perfect-price-api-bmeifqpbwa-el.a.run.app/docs")

# find the search input field
scraping_api = driver.find_element(By.CLASS_NAME, "opblock-summary opblock-summary-get")
#operations-scrape-get_prices_scrape_prices_get > div > button

# scraping_api = driver.find_element(By.CLASS_NAME, "swagger-ui")

# type the search string
# search_field.send_keys("selenium")
#
# # send enter key to get the search results!
# search_field.send_keys(Keys.ENTER)
print(scraping_api)

while(1):
    pass