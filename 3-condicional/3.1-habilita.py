nome = input('digitE seu nome:')
idade = int(input('digite a sua idade:'))


if idade >= 18:
    possui_carteira = input('tem carteira de motorista s/n? ')
    if possui_carteira == "s":
         print('Você pode dirigir')
    else:
         print('não pode dirigir')
         
else:
     print('MENOR DE IDADE')