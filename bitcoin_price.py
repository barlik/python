"""Print bitcoin price."""

import urllib.request
import json

def bitcoin_price():
    """Print bitcoin price"""
    try:
        req = urllib.request.urlopen('https://www.okcoin.com/api/ticker.do?ok=1')
    except urllib.error.HTTPError:
        print('Error loading url.')

    data = json.loads(req.read().decode())

    return data['ticker']['sell']

if __name__ == "__main__":
    print('Price is:', bitcoin_price())
