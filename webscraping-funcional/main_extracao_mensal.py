import time
import pandas as pd
import extracao_mensal

t = time.time()

ano_final_indmensal_analise = 2023
ano_inicial_analise = 2023

numero_tentativas = 5

lst_header = ['DISTRIBUIDORA_ID', 'DISTRIBUIDORA_SIGLA', 'REGIAO', 'INDEX_DIST', 'ANO_INICIO_ANEEL', 'ANO_FIM_ANEEL']
distribuidoras = pd.DataFrame(pd.read_table(r'C:\ConhecendoPython\indic\codigo_distribuidoras-Capitais.txt',
                                            delimiter='	', encoding='ISO-8859-1'), columns=lst_header)

extracao_mensal.EMC(ano_inicial_analise, ano_final_indmensal_analise, numero_tentativas, distribuidoras, 'EMC')

print("escrita finalizada", time.time() - t)
