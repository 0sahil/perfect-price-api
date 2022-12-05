from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

# connect to google.com
driver = webdriver.Chrome(options=Options())
driver.get("https://perfect-price-api-bmeifqpbwa-el.a.run.app/docs")


WebDriverWait(driver, 5).until(presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div["
                                                                      "4]/section/div/span["
                                                                      "3]/div/div/div/span/div/div/button")))
time.sleep(2.5)

driver.find_element(By.XPATH,
                    "/html/body/div/div/div[2]/div[4]/section/div/span[3]/div/div/div/span/div/div/button").click()
time.sleep(2.5)

WebDriverWait(driver, 5).until(presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div["
                                                                      "4]/section/div/span["
                                                                      "3]/div/div/div/span/div/div[2]/div/div[1]/div["
                                                                      "1]/div[2]/button")))
driver.find_element(By.XPATH,
                    "/html/body/div/div/div[2]/div[4]/section/div/span[3]/div/div/div/span/div/div[2]/div/div[1]/div["
                    "1]/div[2]/button").click()
time.sleep(2.5)

input_text = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/section/div/span["
                                           "3]/div/div/div/span/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td["
                                           "2]/input")
input_text.send_keys("iphone")
input_text.send_keys(Keys.RETURN)
time.sleep(2.5)

driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/section/div/span["
                              "3]/div/div/div/span/div/div[2]/div/div[2]/button").click()
time.sleep(20)
