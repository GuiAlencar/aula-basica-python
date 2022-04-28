'''
Condição IF, ELIF e ELSE 
'''

# if False:
#     print("Verdadeiro")
# elif True:
#     print('Agora é verdadeiro')
#     nome = input('Qual o seu nome? : ')
#     print(f'O seu nome é {nome}')
# else:
#     print('Não é verdadeiro')

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, você pode pegar o impréstimo')
else:
    print(f'{nome} você não pode pegar o impréstimo')
