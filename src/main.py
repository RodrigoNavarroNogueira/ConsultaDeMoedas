import requests


def mensagem_de_abertura():
	print('*-' * 30)
	print(f'{" Consulta de Moedas ":=^60}')
	print('*-' * 30)


def exibir_consulta(request, coin, moeda):
    coins = request.json()
    bid = coins[coin]
    if coin == "BTCBRL":
        print(f'Valor do {moeda} atualizado: R${bid["bid"][:6]}')
    else:
        print(f'Valor do {moeda} atualizado: R${bid["bid"][:4]}')
    data = bid["create_date"][:10]
    hora = bid["create_date"][11:19]
    dia = data[8:10]
    mes = data[5:7]
    ano = data[:4]
    print(f'Dia da consulta: {dia}-{mes}-{ano}')
    print(f'Hora: {hora}')
    

    
def escolha_a_opcao():
    option = int(input("""
Selecione a opção que você deseja:
[ 1 ] - Visualizar Dolar
[ 2 ] - Visualizar Euro
[ 3 ] - Visualizar Bitcoin
[ 4 ] - Sair do programa
    """))
    
    if option == 1:
        request = requests.get(f'http://economia.awesomeapi.com.br/json/last/USD-BRL')
        coin = "USDBRL"
        moeda = "dólar"

    elif option == 2:
        request = requests.get(f'https://economia.awesomeapi.com.br/last/EUR-BRL')
        coin = "EURBRL"
        moeda = "euro"

    elif option == 3:
        request = requests.get(f'http://economia.awesomeapi.com.br/json/last/BTC-BRL')
        coin = "BTCBRL"
        moeda = "bitcoin"

    elif option == 4:
        print('Encerrando programa, até logo!')
        exit()

    exibir_consulta(request, coin, moeda)

    nova_consulta = str()

    while nova_consulta == '' or nova_consulta not in 'SN':
        print('--------------------------------------------------------------')
        nova_consulta = input('Deseja realizar uma nova consulta? (S) para SIM e (N) para NÃO\n').upper()

    if nova_consulta == "S":
        escolha_a_opcao()

    elif nova_consulta == "N":
        print('Encerrando programa, até logo!')


mensagem_de_abertura()
escolha_a_opcao()
