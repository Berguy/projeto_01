
import requests

def realdollar():
    real = float (input('Digite o valor em Reais R$: '))
    print()
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    
    requisicao = requisicao.json()
    
    c_dollar = float (requisicao['USDBRL']['bid'])
    
    conversao = real / c_dollar
    
    print(f'{real:.2f} em real representa US$ {conversao:.2f} em dóllar.\n')
	
def dollarreal():
	dollar = float (input('Digite o valor em Dollar US$: '))
	print()
	requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
	
	requisicao = requisicao.json()
	
	c_real = float (requisicao['USDBRL']['bid'])
	
	conversao = dollar * c_real
	
	print(f'{dollar:.2f} em dóllar representa R$ {conversao:.2f} em real.\n')
	
def realeuro():
	real = float (input('Digite o valor em Reais R$: '))
	print()
	requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
	
	requisicao = requisicao.json()
	
	c_euro = float (requisicao['EURBRL']['bid'])
	
	conversao = real / c_euro
	
	print(f'{real:.2f} em real representa EUR$ {conversao:.2f} em euro.\n')

def euroreal():
	euro = float (input('Digite o valor em Euro EUR$: '))
	print()
	requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
	
	requisicao = requisicao.json()
	
	c_real = float (requisicao['EURBRL']['bid'])
	
	conversao = euro * c_real
	
	print(f'{euro:.2f} em euro representa R$ {conversao:.2f} em real.\n')

def realbtc():
	real = float (input('Digite o valor em Reais R$: '))
	print()
	requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
	
	requisicao = requisicao.json()
	
	c_btc = float (requisicao['BTCBRL']['bid'])
	
	conversao = real / c_btc
	
	print(f'{real:.2f} em real representa BTC$ {conversao:.2f} em bitcoin.\n')

def btcreal():
	btc = float (input('Digite o valor em Bitcoin BTC$: '))
	print()
	requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
	
	requisicao = requisicao.json()
	
	c_real = float (requisicao['BTCBRL']['bid'])
	
	conversao = c_real * btc
	
	print(f'{btc:.2f} em bitcoin representa R$ {conversao:.3f} em real.\n')

while True:
    print('Escolha a opção abaixo e digite o número correspondente:\n')
    print('1 - para converter Real em Dóllar \n' '2 - para converter Dóllar em Real \n' '3 - para converter Real em Euro \n' '4 - para converter Euro em Real \n' '5 - para converter Real em Bitcoin \n' '6 - para converter Bitcoin em Real \n')

    opcao = input('Digite apenas números \n')
    print()
    if opcao.isdigit() and opcao.isnumeric():
        match opcao:
            case '1':
                realdollar()
            case '2':
                dollarreal()
            case '3':
                realeuro()
            case '4':
                euroreal()
            case '5':
                realbtc()
            case '6':
                btcreal()
            case _:
                print('Valor inválido!\n' 'Digite apenas números de 1 a 6.\n')
    else:
        print('Valor inválido!\n' 'Digite apenas o número que corresponde a opção desejada.\n')
    if input('Deseja reiniciar (S / N)? ') not in ('S', 's'):
        break
    print()