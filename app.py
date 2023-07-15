from flask import Flask, render_template, request
import requests
import random
import string

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


@app.route('/password-generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        length = int(request.form.get('length'))
        uppercase = 'uppercase' in request.form
        lowercase = 'lowercase' in request.form
        digits = 'digits' in request.form
        special_chars = 'special_chars' in request.form

        chars = ''
        if uppercase:
            chars += string.ascii_uppercase
        if lowercase:
            chars += string.ascii_lowercase
        if digits:
            chars += string.digits
        if special_chars:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        return render_template('password.html', password=password)
    
    return render_template('password_generator.html')

@app.route('/bees')
def bees():
    return render_template('bees.html')

@app.route('/game')
def game():
    return render_template('space.html')

@app.route('/name')
def game():
    return render_template('names.html')

if __name__ == '__main__':
    app.run()