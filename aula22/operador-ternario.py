'''
Operador ternário
'''

# logged_user = False

# msg = 'Usuário Logado.' if logged_user else 'Usuário precisa logar.'

# print(msg)

idade = input('Informe sua idade: ')
if not idade.isnumeric():
    print('Você precisa digitar um número: ')
else:
    idade = int(idade)
    msg = 'Pode acessar' if (idade >= 18) else 'Não pode acessar.'
    print(msg)



