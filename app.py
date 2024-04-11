from flask import Flask, render_template, request
import requests
import random
import string
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cryptos')
def cryptos():
    # Fazendo uma solicitação GET para a API CoinGecko para obter os valores das criptomoedas
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd')
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
def names():
    return render_template('names.html')


@app.route('/cotacoes')
def get_cotacoes():
    # Obtenha as cotações da API
    url = 'https://api.exchangeratesapi.io/latest'
    response = requests.get(url)
    data = response.json()

    # Processar os dados e criar o gráfico de pizza
    # Escolha as moedas que deseja exibir no gráfico
    moedas = ['USD', 'EUR', 'JPY']
    cotacoes = [data['rates'][moeda] for moeda in moedas]

    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(cotacoes, labels=moedas, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Cotações das Moedas')
    # Salvar o gráfico como uma imagem estática
    plt.savefig('static/grafico_pizza.png')

    return render_template('cotacoes.html')


@app.route('/username')
def get_username():
    # Retornar nome do user
    username = str(input('Por favor, digite seu nome: '))
    return username


def welcome_message(username):
    # mensagem de boas vindas ao user
    print(f'Olá, {username} Bem-vindo!')


def main():
    # executa o programa
    username = get_username()
    welcome_message(username)


if __name__ == '__main__':
    app.run()
