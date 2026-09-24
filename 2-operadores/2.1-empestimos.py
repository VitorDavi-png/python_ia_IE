#coletando a situação do correntismo
renda = float(input('digite a sua renda mensal R$ '))
situacao = input("possui retricao / nome negativado (s/n):")

#Validando renda e situação de restrição
emprestimo = (renda >= 3000) and  situacao == "n"

print("emprestimo aprovado?", emprestimo )