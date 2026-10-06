import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["Jardim Belval","Barueri","SP","0645820"],
    ["Parque Santana","Santana de parnaiba","SP","06515-006"],
    ["Subburbano","Itapevi","SP","873589687"],
    ["Centro","Jamdira","SP","547788978"]
]

with open("7.2-cap.csv","w",encoding="utf-8",newline="") as arquivos_csv:
    escrevendo = csv.writer(arquivos_csv)
    escrevendo.writerows(dados_tabela)