from selenium import webdriver
import time

# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)
english_lang_button = driver.find_element_by_css_selector("#promptContentChangeLanguage #langSelect-EN")
english_lang_button.click()
time.sleep(2)

timeout = time.time() + 60*5
while True:
    if time.time() > timeout:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
    big_cookie_button = driver.find_element_by_css_selector("#cookieAnchor #bigCookie")
    big_cookie_button.click()
    try:
        addon_buttons = driver.find_elements_by_css_selector("#products .enabled")
        best_addon_button = addon_buttons[len(addon_buttons) - 1]
    except Exception:
        pass
    else:
        best_addon_button.click()

driver.close()

