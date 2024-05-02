STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import requests
import datetime as dt
from twilio.rest import Client

yesterday_data  = str(dt.date.today() - dt.timedelta(days=2))
day_before_data = str(dt.date.today() - dt.timedelta(days=3))

stock_url = "https://www.alphavantage.co/query"
news_url  = "https://newsapi.org/v2/everything"

stock_key = "enter stock key here"
news_key  = "enter news api key"

#Twilio details
account_sid = 'twilio sid'
auth_token = 'twilio token'
T_NUM = 'twilio num'  #twilio number
R_NUM = 'number' #reciever's number
client = Client(account_sid, auth_token)

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_key
}

news_parameters = {
    "q" : COMPANY_NAME,
    "apiKey" : news_key
}

#calculates and returns the percent change in price 
def calculate_change(yesterday_data, day_before_data):
    change = round(abs(yesterday_data - day_before_data)/yesterday_data * 100, 2)
    if yesterday_data > day_before_data:
        return f"🔺{change}%"
    return f"🔻{change}%"

# fetch stock details
stock_response = requests.get(stock_url, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

#creates a list of data for each day
daily_data = [data for (date,data) in stock_data["Time Series (Daily)"].items()]
yesterday_closing_price  = float(daily_data[0]["4. close"])
day_before_closing_price = float(daily_data[1]["4. close"])


#fetch news and create a list of latest 3 news
news_response = requests.get(news_url, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
top_news = news_data["articles"][:3] #slicing the list and only keeping the first 3 news


#messaging
message = client.messages.create(
        from_= T_NUM,
        body=f"\n{STOCK}: {difference}",
        to= R_NUM
        )

for news in top_news:
    headline = news["title"]
    brief = news["description"]
    message = client.messages.create(
        from_= T_NUM,
        body=f"\nHeadline: {headline}\n\nBrief: {brief}",
        to= R_NUM
        )
