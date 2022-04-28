# x = 0
# while x <= 10:
#     if x == 3:
#         x += 1
#         #continue # volta para o laço
#         break # encerra o laço
#     print(x)
#     x += 1
# print('acabou')

###########################################
# x = 0 # coluna
# while x <= 10:
#     y = 0
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#     x += 1
# print('acabou')
###########################################

# while True:
#     print()
#     num1 = input('Digite um número: ')
#     num2 = input('Digite outro número: ')
#     operador = input('Informe um operador (*/+-): ')
   

#     if not num1.isnumeric() or not num2.isnumeric():
#         print('Você precisa informar um número')
#         continue
    
#     num1 = int(num1)
#     num2 = int(num2)
    
#     if operador == '+':
#         print(num1 + num2)
#     elif operador == '-':
#         print(num1 - num2)
#     elif operador == '/':
#         print(num1 / num2)
#     elif operador == '*':
#         print(num1 * num2)
#     else:
#         print('Operador inválido')
    
#     sair = input('Deseja sair?[s][n]')

#     if sair == 's':
#         break

###########################################

'''
while / else
contadores
acumuladores
'''
contador=0
acumulador = 0

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break 

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
print('Fim programa')
    


