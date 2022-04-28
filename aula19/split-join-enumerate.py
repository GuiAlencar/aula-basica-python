'''
    Split, Join, Enumerate em Python
        * Split - Dividir uma string # str
        * Join - juntar uma lista # str
        * Enumerate - enumerar elementos da lista # list / iteráveis 
'''

########## SPLIT #####################
# string = 'O Brasil é o país do futebol, o Brasil é penta'
# lista1 = string.split(' ')
# lista2 = string.split(',')

# print(lista1)
# print(lista2)

# # for valor in lista1:
# #     print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')

# for valor in lista2:
#     # função strip() tira o espaço do começo e final da frase
#     # função capitalize() deixa a primeira letra maiúscula
#     print(valor.strip().capitalize())



########## JOIN #####################
    
# string = 'O Brasil é penta.'
# lista = string.split()
# string2 = ' '.join(lista)

# print(string)
# print(lista)
# print(string2)

########## Enumerate #####################

# string = 'O Brasil é penta.'
# lista = string.split(' ')

# for indice, valor in enumerate(lista):
#     print(indice, valor)


# lista2 = [
#     [1, 'guilherme'],
#     [3, 'henrique'],
#     [5, 'gontijo'],
# ]

# for indice, nome in lista2:
#     print(indice, nome)

# lista3 = ['Guilherme', 'Henrique', 'Gontijo']

# for indice, nome in enumerate(lista3):
#     print(indice, nome)

## desempacotamento de lista

# lista3 = ['Guilherme', 'Henrique', 'Gontijo']

# n1, n2, n3 = lista3

# print(n2)

#####################

'''
[ <-- enumerate
           0         1         2
    (0, ['Edu',    'João',    'Luiz']), #0
    (1, ['Maria',  'Aline', 'Joana']), #1
    (2, ['Helena', 'Ed',    'Lu']), #2
}
'''

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]
enumerada = list(enumerate(lista))
print(enumerada[1][1][2])