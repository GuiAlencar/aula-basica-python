hora = input('Informe a hora: ')
hora = int(hora)

if hora >=0 and hora <= 11:
    print('Bom dia 0-11')
elif hora > 11 and hora <= 17:
    print('Boa tarde, 12-17')
else: 
    print('Boa noite 18-23')