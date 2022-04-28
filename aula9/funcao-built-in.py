num1 = input('Informe um número: ')
num2 = input('Informe outro número: ')

# isnumeric isdigit isdecimal
# números inteiros e positivos
# print(num1.isnumeric())
# print(num2.isnumeric())

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('Você precisa digitar um número para somar ')