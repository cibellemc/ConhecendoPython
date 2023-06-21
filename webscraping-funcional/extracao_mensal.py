from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def EMC (ano_inicial_analise, ano_final_analise, numero_tentativas, distribuidoras, tipo_extracao):
    # configurações pra não abrir o browser
    hidden_browser = Options()
    hidden_browser.headless = False
    driver = webdriver.Chrome(options=hidden_browser)

    # inicializa o log de registro
    log = 'log_' + tipo_extracao + str(date.today()) + '.txt'
    log = open(log, 'w')
    log.write(str(datetime.now()))
    log.write('\n')

    # inicializa dataframe principal
    df = pd.DataFrame()

    nome_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    for distribuidora in range(len(distribuidoras)):
        regiao = str(distribuidoras['REGIAO'][distribuidora])
        id_distribuidora = str(distribuidoras['DISTRIBUIDORA_ID'][distribuidora])
        sigla_distribuidora = str(distribuidoras['DISTRIBUIDORA_SIGLA'][distribuidora])

        if int(distribuidoras['ANO_INICIO_ANEEL'][distribuidora]) > ano_inicial_analise:
            ano_inicial = int(distribuidoras['ANO_INICIO_ANEEL'][distribuidora])
        else:
            ano_inicial = ano_inicial_analise
        if int(distribuidoras['ANO_FIM_ANEEL'][distribuidora]) < ano_final_analise:
            ano_final = int(distribuidoras['ANO_FIM_ANEEL'][distribuidora])
        else:
            ano_final = ano_final_analise

        for ano in range(ano_inicial, ano_final + 1):
            # ajustar de acordo com mês de referência
            for mes in range(4 , 4 + 1):

                hidden_browser = Options()
                # necessário deixar tela aberta para funcionar
                hidden_browser.headless = False
                driver = webdriver.Chrome(options=hidden_browser)

                for tentativa in range(1, numero_tentativas + 1):

                    try:
                        url = 'https://www2.aneel.gov.br/aplicacoes/indicadores_de_qualidade/DecFecSegMensal.cfm?mes={}&ano={}&regiao={}&distribuidora={}&tipo=d'.format(mes, ano, regiao, id_distribuidora)
                        driver.get(url)

                        element = driver.find_element(By.XPATH, "//table[@class='tab_indice']")
                        html_element = element.get_attribute('outerHTML')
                        soup = BeautifulSoup(html_element, 'html.parser')
                        table = soup.find(name='table')
                        table_str = str(table)

                        df_aux = (pd.read_html(table_str.replace(',', '~'))[0]).replace('~', ',', regex = True)
                        df_aux.drop(df_aux.head(3).index, inplace=True)
                        df_aux.drop(df_aux.tail(3).index, inplace=True)

                        df_aux.insert(loc=0, column= 'ID DISTRIBUIDORA',  value = str(id_distribuidora))
                        df_aux.insert(loc=1, column='PERIODO', value=str('{}/{}'.format(nome_meses[int(mes - 1)], ano)))

                        df = df.append(df_aux)

                        print('{};{};{}/{};tentativa {};ok'.format(tipo_extracao, sigla_distribuidora, nome_meses[int(mes - 1)], ano, tentativa))
                        log.write(str(('{};{};{}/{};tentativa {};ok\n'.format(tipo_extracao, sigla_distribuidora, nome_meses[int(mes - 1)], ano, tentativa))))

                        break
                    except:
                        if tentativa == numero_tentativas:
                            print('{};{};{}/{};tentativa {};erro'.format(tipo_extracao, sigla_distribuidora, nome_meses[int(mes - 1)], ano, tentativa))
                            log.write(str(('{};{};{}/{};tentativa {};erro\n'.format(tipo_extracao, sigla_distribuidora, nome_meses[int(mes - 1)], ano, tentativa))))
                        else:
                            pass
                
            driver.close()
            

    df.columns = ['ID DISTRIBUIDORA', 'PERIODO', 'CONJUNTO',  'COD CONJUNTO', 'NUMERO UCS', 'DECTOT', 'FECTOT',  'DECXP', 'FECXP', 'DECXN', 'FECXN', 'DECIP', 'FECIP', 'DECIND', 'FECIND', 'DECINE', 'FECINE', 'DECINC', 'FECINC', 'DECINO', 'FECINO', 'DECIPC', 'FECIPC', 'DECXPC', 'FECXPC', 'DECXNC', 'FECXNC']

    df = df.astype(str)
    df = df.replace('nan', '', regex=True)

    df.to_csv('resultados/base' + tipo_extracao + '.txt', sep=';', index=False, encoding='utf-8-sig')

    log.close()
