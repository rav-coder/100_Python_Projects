import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

RENTAL_URL = 'https://www.kijiji.ca/b-apartments-condos/calgary/3+bedrooms-house/c37l1700199a27949001a29276001?ad=offering&sort=priceAsc&price=1700__2300&for-rent-by=ownr'
web_page = requests.get(RENTAL_URL).text.encode('unicode_escape').decode()
soup = BeautifulSoup(web_page, 'html.parser')

all_listings = soup.find_all(name='div', class_='clearfix')

for listing in all_listings:
    try:
        rental_info = listing.find_all(name='span', class_='intersection')
        location = rental_info[0].text + ', ' + rental_info[1].text
        # print(location)
        price = listing.select_one(selector='.price').text.strip().split('$')[1].replace('\n', '')\
            .replace(' ', '').replace('n', '').replace('\\', '')
        link = listing.find(name='a', class_='title').get('href')
        # print(price)
        # print(link)
        link = 'https://www.kijiji.ca' + link
        driver.get(
            'https://docs.google.com/forms/d/e/1FAIpQLSda5_PvylKJUPM96vcWViXGM3l_kjbJ4iZZEeAjrhlepVeQDg/viewform')
        sleep(1)

        text_inputs = driver.find_elements_by_css_selector("input[type='text']")
        text_inputs[0].send_keys(location)
        sleep(1)

        text_inputs[1].click()
        text_inputs[1].send_keys(price)
        sleep(1)

        text_inputs[2].click()
        text_inputs[2].send_keys(link)
        sleep(1)

        submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()

    except Exception:
        pass
        # print('not a listing')

driver.quit()







