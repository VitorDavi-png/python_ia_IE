def verificar_idade(idade):
    if  idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
#solicitando a idade dos usuarios
idade_usuario = int(input("Digite sua idade"))

resultado = verificar_idade()
print(resultado)
