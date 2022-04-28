'''
    For in em Python
    Iterando strings com for
    Função range(start=0, stop, step=1)
'''
# texto = 'python'

# for n, i in enumerate(texto):
#     print(n, i)

# for n in range(20, 1, -1):
#     print(n)

# achando os múltiplos de 8
# for i in range(0, 100, 8):
#     print(i)

# print('#########################')

# for i in range(100):
#     if i % 8 == 0:
#         print(i)

texto = 'python'
nova_string = ''

for i in texto:
    if i == 't':
        nova_string += i.upper()        
    elif i == 'h':
        nova_string += i.upper()
    else:
        nova_string += i
print(nova_string)