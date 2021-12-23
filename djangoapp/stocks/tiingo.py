import requests

headers = {
    'Content-Type':'application/json',
    'Authorization': 'Token f0e5b7d023cc30ba70e68c21152d64c3dec5dfc7'

}
def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()

def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]

