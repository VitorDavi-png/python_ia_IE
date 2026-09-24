def maior_numer(x,y):
    if x > y:
        return x
    else:
        return y

numero_1=float(input("Digite um numero: "))
numero_2=float(input("digite o segundo numero: "))
resu= maior_numer(numero_1,numero_2)

print(f"MAIOR NUMERO DIGITADO FOI{resu}")