lista_inicial = ["joão","pamela","dominique"]

print("lista inicial", lista_inicial)
print(60 * "-")

lista_inicial.append("Eduarda")
print("apos append", lista_inicial)
print(60 * "-")

lista_inicial.insert(2,"Matheus")
print("apos insert", lista_inicial)
print(60 * "-")

lista_inicial[3] = "Rafael"
print("apos moficação", lista_inicial)
print(60 * "-")

del lista_inicial[3]
print("após del:",lista_inicial)
print(60 * "-")

lista_inicial.remove("pamela")
print("após remove:",lista_inicial)
print(60 * "-")

removido = lista_inicial.pop(1)
print(f"após pode,removido {removido}:",lista_inicial)
print(60 * "-")

lista_inicial.clear()

print("após clar" ,lista_inicial)
print(60 * "-")