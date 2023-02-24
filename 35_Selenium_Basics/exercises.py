from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

# driver.get('https://www.amazon.ca/gp/product/B086MKMW4B/ref=ox_sc_saved_title_3?smid=A3P4UZIS42PRQV&psc=1')
# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# python_logo = driver.find_element_by_class_name("python-logo")
# print(python_logo.size)
# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

## find by XPath
link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(link.text)

# driver.close()  # closes one tab
driver.quit()  # closes the browser, all tabs

events_div = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events = events_div.find_elements_by_tag_name(name="li")

events_dict = {}
for index, event in enumerate(events):
    name = event.find_element_by_tag_name(name="a").text
    date = event.find_element_by_tag_name(name="time").text
    events_dict[f"{index}"] = {
        "name": name,
        "date": date,
    }

print(events_dict)
