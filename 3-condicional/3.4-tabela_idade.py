nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))

if idade <1:
    resultado = ("Recém nascido")
elif idade <3:
    resultado = ("Bebê")
elif idade <10:
    resultado =("criança")
elif idade <13:
    resultado =("Pré-Adloscente")
elif idade <18:
    resultado =("Adolescente")
elif idade <60:
    resultado =("Adulto")
else:
    resultado =("Idoso")

    print(f"olá {nome} para sua faixa etária voçê é uma {resultado}")