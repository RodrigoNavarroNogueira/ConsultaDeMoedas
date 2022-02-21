import requests


def mensagem_de_abertura():
	print('*-' * 30)
	print(f'{" Consulta de Moedas ":=^60}')
	print('*-' * 30)


def escolha_a_opcao():
    option = int(input("""
Selecione a opção que você deseja:
[ 1 ] - Visualizar Dolar
[ 2 ] - Visualizar Euro
    """))
    
    if option == 1:
        request = requests.get(f'http://economia.awesomeapi.com.br/json/last/USD-BRL')
        
    elif option == 2:
        request = requests.get(f'https://economia.awesomeapi.com.br/last/EUR-BRL')


    coins = request.json()
    bid = coins["USDBRL"]
    print(f'Valor do dólar atualizado: R${bid["bid"][:4]}')
    print(f'Dia e hora da consulta: {bid["create_date"]}')



mensagem_de_abertura()
escolha_a_opcao()


