import os
import requests
import boto3
from chalice import Chalice
app = Chalice(app_name='AppName')
app.debug = True


@app.route("/")
def index():
    url = 'https://api.ethplorer.io/getTokenInfo/0x2b89bf8ba858cd2fcee1fada378d5cd6936968be?apiKey=freekey'
    r = requests.get(url)
    response = r.json()
    price = response["price"]["rate"]
    symbol = response["symbol"]
    answer = str(symbol) + " = " + str(price)
    print("Hello")
    return answer
