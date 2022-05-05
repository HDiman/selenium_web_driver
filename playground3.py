from selenium import webdriver
import time

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# url = "http://www.google.com/"
# url = "https://yandex.ru/"
# url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=sr_1_3?crid=FQ86UAZ13OI9&keywords=instant%2Bpot&qid=1651740011&sprefix=insta%2Caps%2C253&sr=8-3&th=1"
# class_="a-price"
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/selenium_web_driver/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(doc_link.text)

website_bug = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(website_bug.get_attribute('href'))

driver.close()
driver.quit()
