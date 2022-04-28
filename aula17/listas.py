'''
    Listas em Python
    fatiamento
    append, insert, pop, del, clear, extend
    min, max
    range
'''
#         0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']

# fatiamento de lista
# print(lista[:3])
# print(lista[-1])
# print(lista[::2])
# print(lista[::-1]) # de forma invertida


# for i in range(len(lista)):
#     if lista[i] == 'A':
#         lista[i] = 'Guilherme'
#     else:
#         lista[i] = lista[i] 
# print(lista)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# l3 = l1 + l2 
# l1.extend(l2)

# print(l2)
# l2.append('a')
# #inserindo dados onde eu quiser, usando insert(índice, 'qualquer coisa')
# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# # apagando o último valor da lista com pop
# l2.pop()
# print(l2)
# # print(l1)
# # print(l3)
# del(l2[0])
# # del(l2[:7])
# print(l2)

# pegando o valor máximo e o mínimo da lista l2
# print(max(l2))
# print(min(l2))

# usando a função range para escrever de 0 a 9
# l4 = list(range(0, 10, 2))
# l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(l4)

# for i in l4:
#     print(i)

# l4 = ['string', True, 10, -20.5]

# for elemento in l4:
#     print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')

############################################################

secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!!')
        continue 

    digitadas.append(letra)
    
    if letra in secreto:
        print(f'acertou!! A letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()
   
    secreto_temp = ''
    for i in secreto:
        if i in digitadas:
            secreto_temp += i
        else:
            secreto_temp += '*'
    
    if secreto_temp == secreto:
        print(f'Você ganhou o jogo!!\o/ A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
        

