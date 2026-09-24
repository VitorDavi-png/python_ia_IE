#Solicitando idade e se é estudante
idade = int(input('Digite sua idade: '))
estudante = input('você é estudadnte s/n :')

#Validando meia-entrada 
verificao = (idade >= 60) or estudante == "s"

#Apresntando o resultado
print("tem direito a meia entrada,", verificao)