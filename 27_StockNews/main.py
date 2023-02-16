import requests
from decouple import config
from datetime import date, timedelta
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "RSLS"
COMPANY_NAME = "Reshape"
STOCK_API_KEY = config('STOCK_API_KEY')
NEWS_API_KEY = config("NEWS_API_KEY")

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
FROM_NUM = config('TWILIO_PHONE_NUM')
TO_NUM = config('MOBILE_NUM')

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

YESTER_DATE = str(date.today() - timedelta(days=1))
DAY_BEF_YES_DATE = str(date.today() - timedelta(days=2))

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchin": "title",
    "from": DAY_BEF_YES_DATE,
    "to": YESTER_DATE,
    "sortBy": "popularity",
}


def closing_percent_diff():
    response = requests.get("https://www.alphavantage.co/query", params=stock_params)
    response.raise_for_status()
    all_stock_data = response.json().get("Time Series (Daily)")

    yester_price = float(all_stock_data.get(YESTER_DATE).get("4. close"))
    day_bef_yes_price = float(all_stock_data.get(DAY_BEF_YES_DATE).get("4. close"))

    percent_diff = ((yester_price - day_bef_yes_price) * 100) / day_bef_yes_price
    return round(percent_diff, 2)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_top_3_news():
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    return news_data.get("articles")[:3]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if abs(closing_percent_diff()) >= 5:
    top_3_news = get_top_3_news()
    print(top_3_news)
    if closing_percent_diff() < 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    for news in top_3_news:
        message = f"{STOCK}: {symbol}{closing_percent_diff()}% \n\n" \
                  f"Headline: {news.get('title')}\n\n" \
                  f"Article: {news.get('url')}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=FROM_NUM,
            to=TO_NUM,
        )
        print(message.status)
