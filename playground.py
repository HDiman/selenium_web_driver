# from selenium import webdriver
#
# chrome_driver_path = "/Users/dsannikov/Development"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://www.amazom.com")
# driver.get("https://www.billboard.com/charts/hot-100/")

import time
from selenium import webdriver

chrome_driver_path = "/Users/dsannikov/Development"
driver = webdriver.Chrome(executable_path=chrome_driver_path)  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

# time.sleep(5) # Let the user actually see something!
#
# search_box = driver.find_element_by_name('q')
#
# search_box.send_keys('ChromeDriver')
#
# search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
