# for / else 

lista = ['Guilherme', 'Henrique', 'Gontijo']
# startswitch, verifica a primeira letra da string
# for i in lista:
#     if i.startswith('G'):
#         print(f'{i} começa com G')
#     else:
#         print(f'{i} não começa com G')

########################################################################

# comeca_com_g = False 
# cont = 0
# for i in lista:
#     if i.lower().startswith('g'):
#         comeca_com_g = True 
#         cont += 1
# if comeca_com_g:
#     print(f'Existe {cont} palavra(s) que começa com G.')
# else:
#     print('Não existe palavra que começa com G')

########################################################################

for i in lista:
    print(i)
    if i.lower().startswith('g'):
        break
else:
    print('Não existe palavra que começa com G')