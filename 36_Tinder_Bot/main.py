from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from decouple import config

# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

driver.get("https://tinder.com/")
time.sleep(1)

log_in_button = driver.find_element_by_xpath('//*[@id="t-1958763962"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

time.sleep(1)

google_login = driver.find_element_by_xpath('//*[@id="t607822258"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
google_login.click()


# https://tinder.onelink.me/9K8a/3d4abb81