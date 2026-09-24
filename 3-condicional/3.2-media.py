#solicitando nome e otas
nome = input("Digite seu nome: ")
nota_1 = float(input("digite sua primeira nota: "))
nota_2 = float(input("digite sua segunda nota: "))
nota_3 = float(input("digite sua terceira nota: "))

#Reaizando o calculo
media =(nota_1 + nota_2 + nota_3 ) /3


 
if media <4 :
    situacao =("Reprovado Burro")
elif media <=6:
    situacao =('Recuperação')
else:
    situacao =('Aprovado')

print(f"A media do aluno(a) {nome} é {media:.2f} e voçê foi {situacao}")

