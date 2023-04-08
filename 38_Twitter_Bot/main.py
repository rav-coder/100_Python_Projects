from decouple import config
from selenium import webdriver
from time import sleep

PROMISED_UPLOAD = 500
PROMISED_DOWNLOAD = 100

# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)

driver.get('https://www.speedtest.net/')

go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
go_button.click()
sleep(50)

# data_div = driver.find_element_by_css_selector('.result-container-data')

download_speed = float(driver.find_element_by_css_selector('.download-speed').text)
upload_speed = float(driver.find_element_by_css_selector('.upload-speed').text)

print(f'{download_speed}, {upload_speed}')


def login_twitter():
    twitter_button = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/a[2]')
    twitter_button.click()

    sleep(2)
    log_in_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]')
    log_in_button.click()

    sleep(2)
    email_input = driver.find_elements_by_tag_name('input')
    email_input.send_keys(config('USER'))
    next_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()

    sleep(2)
    pass_input = driver.find_element_by_name('password')
    pass_input.send_keys(config('PASS'))
    log_in_final_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    log_in_final_button.click()


def send_tweet():
    tweet_text = f'Hey ISP why do I get {download_speed}down/ {upload_speed}up when my internet speed is supposed to' \
                 f'be {PROMISED_DOWNLOAD}down/ {PROMISED_UPLOAD}up ?'

    tweet_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div')
    tweet_input.send_keys(tweet_text)

    tweet_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    tweet_button.click()
    driver.quit()


if (PROMISED_DOWNLOAD - download_speed) > 20 or (PROMISED_UPLOAD - upload_speed) > 20:
    sleep(2)
    login_twitter()
    sleep(2)
    send_tweet()





