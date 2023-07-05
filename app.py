from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cryptos')
def cryptos():
    # Fazendo uma solicitação GET para a API CoinGecko para obter os valores das criptomoedas
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd')
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        ethereum_price = data['ethereum']['usd']
    else:
        bitcoin_price = None
        ethereum_price = None

    return render_template('cryptos.html', bitcoin_price=bitcoin_price, ethereum_price=ethereum_price)

@app.route('/cat')
def cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        data = response.json()
        cat_url = data[0]['url']
    else:
        cat_url = None

    return render_template('cat.html', cat_url=cat_url)

if __name__ == '__main__':
    app.run()