def cal_soma(x,y):
    soma = x + y
    return soma

def cal_sub(x,y):
    subtr = x - y
    return subtr

def cal_div(x,y):
    divi = x / y
    return divi

def cal_mult(x,y):
    multi = x * y
    return multi

numero_1 = float(input("digite um numero: "))
numero_2 = float(input("digite o segundo numero:"))

print(cal_soma (numero_1,numero_2))
print(cal_sub(numero_1,numero_2))
print(cal_div(numero_1,numero_2))
print(cal_mult(numero_1,numero_2))

