'''
Formatando valores com modificadores
:s - texto (strings)
:d - int
:f - float
:.(número)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
> - esquerda
< - direita
^ - centro
'''

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print(f'{divisao:.2f}')

# num1 = 1
# print(f'{num1:0^10}')
# print(f'{num1:0>10}')
# print(f'{num1:0<10}')

# num2 = 1150
# print(f'{num2:0>10.2f}')

# nome = 'Guilherme Alencar'
# print(f'{nome:#^40}')

nome = 'guilherme alencar'
print(nome.lower())
print(nome.upper())
print(nome.title())