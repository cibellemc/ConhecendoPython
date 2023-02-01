from selenium import webdriver
from datetime import date, datetime
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def RMD (ano_inicial_analise, ano_final_analise, numero_tentativas, distribuidoras, tipo_extracao):
    # CONFIGURA PARA NÃO ABRIR PÁGINA DO NAVEGADOR
    hidden_browser = Options()
    hidden_browser.headless = True
    driver = webdriver.Chrome(options=hidden_browser)

    # SE TENTAR ACESSAR DÁ ERRO, POIS FALTA A REGIÃO
    endereco = 'https://www2.aneel.gov.br/aplicacoes_liferay/indicadores_de_qualidade/pesquisa.cfm?regiao='

    # ANOTA ERROS (NÃO TÁ FUNFANDO
    log = 'log_' + tipo_extracao + str(date.today()) + '.txt'
    log = open(log, 'w')
    log.write(str(datetime.now()))
    log.write('\n')

    df = pd.DataFrame()

    for distribuidora in range(len(distribuidoras)):
        # PD DAS DISTRIBUIDORAS[COLUNA][NÚMERO DA EXECUÇÃO CORRENTE]
        regiao = str(distribuidoras['REGIAO'][distribuidora])
        id_distribuidora = str(distribuidoras['DISTRIBUIDORA_ID'][distribuidora])
        sigla_distribuidora = str(distribuidoras['DISTRIBUIDORA_SIGLA'][distribuidora])

        # COLOCA A REGIÃO NO FIM DO LINK
        url = endereco + regiao

        # SE O ANO INÍCIO ANEEL (2000) FOR MAIOR QUE O ANO INICIAL INFORMADO NA MAIN
        if int(distribuidoras['ANO_INICIO_ANEEL'][distribuidora]) > ano_inicial_analise:
            ano_inicial = int(distribuidoras['ANO_INICIO_ANEEL'][distribuidora])
        else:
            ano_inicial = ano_inicial_analise

        # SE O ANO FIM ANEEL (2999) FOR MENOR QUE O ANO FINAL INFORMADO NA MAIN
        if int(distribuidoras['ANO_FIM_ANEEL'][distribuidora]) < ano_final_analise:
            ano_final = int(distribuidoras['ANO_FIM_ANEEL'][distribuidora])
        else:
            ano_final = ano_final_analise

        for ano in range(ano_inicial, ano_final + 1):

            # TENTATIVAS INFORMADAS NA MAIN (NO CASO DE 1 A 6
            for tentativa in range(1, numero_tentativas + 1):
                multiplicador_tempo = tentativa
                try:
                    driver.get(url)
                    select_tipo = Select(driver.find_element(By.NAME, 'tipo'))
                    select_tipo.select_by_value('g')
                    sleep(multiplicador_tempo * 0.5)
                    select_tipoE = Select(driver.find_element(By.NAME, 'tipoE'))
                    select_tipoE.select_by_value('c')
                    sleep(multiplicador_tempo * 0.5)
                    select_dist = Select(driver.find_element(By.NAME, 'distribuidora'))
                    select_dist.select_by_value(str(id_distribuidora))
                    sleep(multiplicador_tempo * 0.5)
                    select_periodo = Select(driver.find_element(By.NAME, 'periodo'))
                    select_periodo.select_by_value('1')
                    sleep(multiplicador_tempo * 0.5)
                    select_ano = Select(driver.find_element(By.NAME, 'ano'))
                    select_ano.select_by_value(str(ano))
                    sleep(multiplicador_tempo * 0.15)
                    driver.find_element(By.ID,'submit_obter_dados').click()
                    sleep(multiplicador_tempo * 0.15)

                    #
                    driver.switch_to.window(driver.window_handles[1])

                    element = driver.find_element(By.XPATH, '/html/body/div/table[1]')
                    html_element = element.get_attribute('outerHTML')
                    soup = BeautifulSoup(html_element, 'html.parser')
                    table = soup.find(name='table')
                    table_str = str(table)

                    df_aux = pd.DataFrame()
                    df_aux = (pd.read_html(table_str.replace(',', '~'))[0]).replace('~', ',', regex=True)
                    df_aux.drop(df_aux.head(2).index, inplace=True)

                    tamanho_coluna = len(driver.find_element(By.XPATH, '/html/body/div/table[1]/tbody[1]/tr[3]/td').text)

                    df_aux = df_aux.loc[:, 1:tamanho_coluna - 1]
                    df_aux = df_aux.T
                    df_aux = df_aux.dropna(axis=0, how='all')

                    df_aux.insert(loc=0, column='ID DISTRIBUIDORA', value=str(id_distribuidora))
                    df_aux[2] = df_aux[2] + '/' + str(ano)


                    df = df.append(pd.DataFrame(df_aux))

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    print('{};{};{};tentativa {};ok'.format(tipo_extracao, sigla_distribuidora, ano, tentativa))
                    log.write(str(('{};{};{};tentativa {};ok\n'.format(tipo_extracao, sigla_distribuidora, ano, tentativa))))
                    break
                except:
                    if tentativa == numero_tentativas:
                        print('{};{};{};tentativa {};erro'.format(tipo_extracao, sigla_distribuidora, ano, tentativa))
                        log.write(str(('{};{};{};tentativa {};erro\n'.format(tipo_extracao, sigla_distribuidora, ano, tentativa))))
                    else:
                        pass

    df.columns = ['ID DISTRIBUIDORA', 'PERIODO', 'DEC',  'FEC',  'NUMERO UCS']

    df = df.astype(str)
    df = df.replace('nan', '', regex=True)

    df.to_csv('base' + tipo_extracao + '.txt', sep=';', index=False, encoding='utf-8-sig')

    log.close()

