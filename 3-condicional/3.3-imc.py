#solicitando dados dos pacientes
nome = input("digite o nome do paciente: ")
altura = float(input('digite a altura em M:'))
peso = float(input("digite peso em kg: "))

#Calculando o IMC do paciente
imc = peso/altura**2

#definindo o quadro pelo iMC
if imc <16:
    reusltado = ("Magreza Grave")
elif imc <17:
    reusltado = ("Magreza Moderada")
elif imc <18.5:
    reusltado = ("Magreza Leve")
elif imc <25:
    reusltado = ("saudavel")
elif imc <30:
    reusltado = ("Sobrepeso")
elif imc <35:
    reusltado = ("Obesidade Grau 1")
elif imc <40:
    reusltado = ("Obesidade Grau 2(Severa)")
else:
    reusltado = ("Obesidade Grau 3(Mórbida)")

print(f"olá paciente {nome} seu imc é {imc:.2f} e você está com {reusltado}")