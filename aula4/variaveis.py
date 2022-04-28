nome = 'Guilherme'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
