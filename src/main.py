import requests


def mensagem_de_abertura():
	print('*-' * 30)
	print(f'{" Consulta de Moedas ":=^60}')
	print('*-' * 30)


mensagem_de_abertura()

request = requests.get(f'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

coins = request.json()

if 'erro' not in coins:
	print(request.json())

else:
	print('Moeda inválida')
	while True:
		new_try = int(input('Você deseja realizar uma nova consulta? (1) Para SIM e (2) Para NÃO\n'))




