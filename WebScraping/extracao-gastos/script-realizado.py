import  jpype     
import datetime
import pandas as pd
import asposecells # linha necessária
jpype.startJVM() 
from asposecells.api import Workbook

with open('<>\\2209-realizado.txt', 'r', encoding='ansi') as arquivo_original:
    # lê todo o conteúdo do arquivo original e armazena na variável 'conteudo' como texto na codificação original (ANSI)
    conteudo = arquivo_original.read()

# novo arquivo para escrita com codificação UTF-8
with open('<>\\2209-realizado.txt', 'w', encoding='utf-8') as arquivo_utf8:
    # escreve o conteúdo no novo arquivo - o mesmo do arquivo original, mas em UTF-8
    arquivo_utf8.write(conteudo)

workbook = Workbook("<>\\2209-realizado.txt")
workbook.save("<>\\2209-realizado.xlsx")

jpype.shutdownJVM()

df = pd.read_excel('<>\\2209-realizado.xlsx', skiprows=35)
df = df.dropna(axis=1, how='all')

# converte o DataFrame em uma lista de dicionários
result = []
for col in df.columns[1:]:
    pacote = df[col].name
    gastos = []
    for i, row in df.iterrows():
        if i >= 0:
            mes = row['Classes de custo']
            valor = row[col]
            gastos.append({"Valor": valor, "Mês": mes})
    result.append({"Pacote": pacote, "Gasto": gastos})

df = pd.json_normalize(result, 'Gasto', ['Pacote'])
df.columns = ['Valor', 'Subpacote', 'Mês']
df['Mês'] = df['Mês'].str.strip()
df['Tipo'] = "REALIZADO"

# Configuração de nome de arquivo
agora = datetime.datetime.now()
agora_string = agora.strftime("%d-%m-%y")

df.to_excel('<>\\' + 'realizado_' + agora_string + '.xlsx', index=False)
