from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/selenium_web_driver/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)

upcoming_event = {}
for i in range(5):
    event_time = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[3]/div[2]/div/ul/li[{i+1}]/time")
    event_title = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[3]/div[2]/div/ul/li[{i+1}]/a")
    upcoming_event[i] = {
        "time": event_time.text,
        "name": event_title.text,
    }
print(upcoming_event)

driver.close()
driver.quit()
