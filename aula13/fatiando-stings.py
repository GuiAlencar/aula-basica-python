'''
Manipulando strings
Strings indices
fatiamento de strings [inicio:fim:passo]
Funções built-in len, abs, type, print
Essas funções podem ser usadas diretamente em cada tipo.
'''

texto = 'Python s2'
print(texto[2])

# url = 'www.google.com.br/'
# removendo a barra da url
# print(url[:-1])

#começando do índice 2 até o índice 6
nova_string = texto[2:6]
print(nova_string)
######################################

#começando do índice 0 até o índice 6
nova_string = texto[1:6]
print(nova_string)
######################################

#começando do índice 0 até o índice 6 e pegando de dois em dois
nova_string = texto[0:6:2]
print(nova_string)
######################################