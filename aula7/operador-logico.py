'''
Operadores Lógicos
and, or, not
int e not in
'''
# a = 2
# b = 3

# if not b > 2:
#     print('B é maior do que A')
# else:
#     print('A é maior do que B')

# nome = 'Guilherme'
# if 'Gui' in nome:
#     print('Existe a letra Gui no seu nome')
# else:
#     print('Não existe')

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

if senha == '123456':
    print('Acesso permitido')
    print(f'Bem vindo, {usuario}')
else:
    print('Acesso Negado')
