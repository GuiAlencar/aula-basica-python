numero = input('Informe um número: ')

try:
    numero = int(numero)
    if numero % 2 == 0:    
        print(f'O número {numero} é par')
    else:
        numero = int(numero)
        print(f'O número {numero} é ímpar')
except:
    print('Por favor informe um número e com valor inteiro')
