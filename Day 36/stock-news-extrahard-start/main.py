import requests
import os
from dotenv import load_dotenv
load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters_stocks={
    "symbol":"TSLA",
    "function":"TIME_SERIES_DAILY",
    "apikey":os.environ.get("STOCK_API_KEY")
}
response=requests.get("https://www.alphavantage.co/query?",params=parameters_stocks)
response.raise_for_status()
data=response.json()
data2=list((data["Time Series (Daily)"]).values())
yesterday_data=float(data2[0]['4. close'])
day_before=float(data2[1]['4. close'])
dates=list((data["Time Series (Daily)"]).keys())
percentage=round(((yesterday_data-day_before)/day_before*100),4)

if percentage<0 and abs(percentage)>5:
    print(f"The stock has decreased by {percentage}. Might wanna consider to sell")
elif percentage>0 and abs(percentage)>5:
    print(f"The stock has increased by {percentage}. Hold on and sell at right time.")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api=os.environ.get("NEWS_API_KEY")
parameters={
    "q":"Tesla",
    "from":"2026-07-15",
    "sortBy":"popularity",
    "apiKey":news_api
}
response2=requests.get("https://newsapi.org/v2/everything?",params=parameters)
response2.raise_for_status()
data2=response2.json()
print(data2)