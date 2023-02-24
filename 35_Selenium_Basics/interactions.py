from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"
# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

# driver.get(WIKI_URL)
# # count = driver.find_element_by_id("articlecount")
# # print(count.text.split(" ")[0].strip(','))
# article_link = driver.find_element_by_css_selector("#articlecount a")
# # article_link.click()
#
# wiktionary_link = driver.find_element_by_link_text("Wiktionary")
# # wiktionary_link.click()
#
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
first_name_field = driver.find_element_by_name("firstname")
first_name_field.send_keys("Testing")

last_name_field = driver.find_element_by_name("lastname")
last_name_field.send_keys("Hello")

submit_button = driver.find_element_by_name("submit")
submit_button.click()




