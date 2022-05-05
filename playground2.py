from selenium import webdriver
import time
# from fake_useragent import UserAgent

# ua = UserAgent()

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# url = "http://www.google.com/"
# url = "https://yandex.ru/"
# url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=sr_1_3?crid=FQ86UAZ13OI9&keywords=instant%2Bpot&qid=1651740011&sprefix=insta%2Caps%2C253&sr=8-3&th=1"
# class_="a-price"
url = "https://www.python.org/"

# Options
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld!")

chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/selenium_web_driver/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.implicitly_wait(10)
# price = driver.find_element("a-price")
# print(price)

time.sleep(5)
driver.close()
driver.quit()

# try:
#     driver.get(url=url)
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()






# driver.get("https://www.billboard.com/charts/hot-100/")

# import time
# from selenium import webdriver
#
# chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/selenium_web_driver/driver/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)  # Optional argument, if not specified will search path.
#
# driver.get('http://www.google.com/')

# time.sleep(5) # Let the user actually see something!
#
# search_box = driver.find_element_by_name('q')
#
# search_box.send_keys('ChromeDriver')
#
# search_box.submit()
#
# time.sleep(5) # Let the user actually see something!
#
# driver.quit()