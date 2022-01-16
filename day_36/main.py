# TRADING APP
import requests
import os
import math
from datetime import datetime, timedelta


def run():
    # Date variables, to get today and yesterday dates in a format that the JSON
    # stock_response data may find those dates
    today = datetime.today()
    today_formatted = today.strftime('%Y-%m-%d')
    yesterday = today - timedelta(days=1)
    yesterday_formatted = yesterday.strftime('%Y-%m-%d')

    # STOCKS CONSTANTS
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla"
    STOCK_KEY = os.environ["STOCK_KEY_ENV"]
    stock_api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_KEY,
    }

    # STEP 1: Use https://www.alphavantage.co
    STOCK_ENDPOINT = 'https://www.alphavantage.co/query?'
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_api_params)
    stock_response.raise_for_status()
    data = stock_response.json()

    # Find the final values when close the market
    yesterday_final_value = float(data["Time Series (Daily)"][yesterday_formatted]['4. close'])
    today_final_value = float(data["Time Series (Daily)"][today_formatted]['4. close'])

    # When STOCK price increases/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    # % variation = (( V2 - V1 ) /V1) * 100
    percentage_variation = ((today_final_value - yesterday_final_value) / yesterday_final_value) * 100
    percentage_variation = round(percentage_variation, 2)
    print(percentage_variation, "%")

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API_KEY_ENDPOINT = "https://newsapi.org/v2/top-headlines?"
    NEWS_API_KEY = os.environ["NEWS_API_KEY_ENV"]
    news_api_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    if (percentage_variation >= 5) or (percentage_variation <= -5):
        print(f"Get news.The variation is {percentage_variation}%.")
        news_response = requests.get(url=NEWS_API_KEY_ENDPOINT, params=news_api_params)
        news_data = news_response.json()
        new_1 = news_data["articles"][2]["title"]
        new_2 = news_data["articles"][3]["title"]
        new_3 = news_data["articles"][4]["title"]
        print(new_1)
        print(new_2)
        print(new_3)
    else:
        print(f"Normal, the variation is {percentage_variation}%.")

    ## STEP 3: Send a message to your whatsapp
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    # TODO: Do this step with WhatsApp instead of SMS, WhatsApp is free

    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """


# Entry point
if __name__ == '__main__':
    run()
