import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "sample_sid"
auth_token = "sample_token"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "sample_key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "sample_key"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
res = requests.get(STOCK_ENDPOINT, params=stock_params)
data = res.json()['Time Series (Daily)']
data_list = [value for key, value in data.items()]
yesterday_c_price = data_list[0]["4. close"]
day_before_yesterday_c_price = data_list[1]["4. close"]

diff = float(yesterday_c_price) - float(day_before_yesterday_c_price)
diff_percentage = (abs(diff) / float(yesterday_c_price)) * 100


if diff_percentage > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    res = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = res.json()["articles"]
    three_articles = news_data[:3]
    f_articles = [f"Headline {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    for f_article in f_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f_article,
            from_="+14-8202019292",
            to="+84909891252"
        )
