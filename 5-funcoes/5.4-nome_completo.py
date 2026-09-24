def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"

nome_use =input("digite o seu nome: ")
sobrenome_usuario =input("digite o seu sobrenome:")

nome_int = nome_completo(nome_use,sobrenome_usuario)

print(f"bem vindo,{nome_int}")