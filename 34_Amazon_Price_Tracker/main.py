import requests
from bs4 import BeautifulSoup
import smtplib
from decouple import config

GMAIL_USER = config("GMAIL_USER")
GMAIL_PASS = config("GMAIL_PASS")

PRICE_TO_WATCH = 37
ITEM_URL = "https://www.amazon.ca/gp/product/B086MKMW4B/ref=ox_sc_saved_title_3?smid=A3P4UZIS42PRQV&psc=1"
headers = {
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50",
    "User-Agent": "en-US,en;q=0.9",
}

response = requests.get(url=ITEM_URL, headers=headers)
url_content = response.text
soup = BeautifulSoup(url_content, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole").text.strip(".")
price_decimal = soup.find(name="span", class_="a-price-fraction").text
item_price = float(f"{price_whole}.{price_decimal}")
# print(item_price)
product_title = soup.find(name="span", id="productTitle").text.strip()

if item_price <= PRICE_TO_WATCH:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASS)
        connection.sendmail(from_addr=GMAIL_USER,
                            to_addrs=GMAIL_USER,
                            msg=f"Subject: Amazon Low Price Alert!\n\n"
                                f"Item: {product_title} \n\n"
                                f"Is on Sale for {item_price} CAD\n\n"
                                f"Link: {ITEM_URL}")
