nome = input('Informe seu nome: ')
qtd_caracter = len(nome)

if qtd_caracter <= 4:
    print('Seu nome é curto!!')
elif qtd_caracter >= 5 and qtd_caracter <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')