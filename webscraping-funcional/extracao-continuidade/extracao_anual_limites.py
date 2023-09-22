import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 30)
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

estados = []
municipios = []
anos = []
df_urb = pd.DataFrame()


def atualiza_html_e_conta_options(tempo_sleep, nome_elemento):
    sleep(tempo_sleep)

    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    lista_E = conteudo_web.find('select', {'id': f'frm{nome_elemento}'})

    return int(len(lista_E) / 2)


def seleciona_elemento(nome_elemento, nome_contador):
    selecao = Select(navegador.find_element(By.XPATH, f'//*[@id="frm{nome_elemento}"]'))
    selecao.select_by_index(nome_contador)


def cria_lista(nome_elemento):
    # sleep(2)
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    find_el = conteudo_web.find("select", {"id": f"frm{nome_elemento}"}).get_text()
    return find_el.split('\n')


def tables(indice_table):
    locator = (By.XPATH, '//*[@id="resposta"]/table[2]')
    wait.until(ec.presence_of_element_located(locator))
    web = BeautifulSoup(navegador.page_source, 'html.parser')
    tabelas = web.find('div', {'id': 'resposta'}).find_all('tr', {'class': 'res'})

    tabela1 = tabelas[indice_table].text.strip().upper().split("\n")

    df1 = pd.DataFrame(tabela1).replace(',', '.', regex=True).transpose()
    sleep(1)

    return df1


for e in range(18, 19):
    seleciona_elemento('Estados', e)
    lista_estados = cria_lista('Estados')
    qtd_municipios = atualiza_html_e_conta_options(2, 'Municipios')

    for m in range(51, 150):
        seleciona_elemento('Municipios', m)
        lista_municipios = cria_lista('Municipios')
        qtd_anos = atualiza_html_e_conta_options(1, 'Anos')

        for a in range(13, 14):
            seleciona_elemento('Anos', a)
            lista_anos = cria_lista('Anos')
            qtd_conjuntos = atualiza_html_e_conta_options(1.5, 'Conjuntos')

            for c in range(1, qtd_conjuntos):
                seleciona_elemento('Conjuntos', c)
                lista_conjuntos = cria_lista('Conjuntos')
                df1 = tables(0)
                df_urb = df_urb.append(df1, ignore_index=True)

                estados.append(lista_estados[e + 1])
                municipios.append(lista_municipios[m + 1].strip())
                anos.append(lista_anos[a + 1])

df_urb.columns = ['Conjunto', 'DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']
df_urb[['DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']] = \
df_urb[['DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']].apply(pd.to_numeric)
zip = list(zip(estados, municipios, anos))
df_estmunanocon = pd.DataFrame(zip, columns=['Estado', 'Município', 'Ano'])
m = pd.merge(df_estmunanocon, df_urb, right_index=True, left_index=True, how='outer')
print(m)
m.to_excel("indicadorespi2022.xlsx", sheet_name='Baixa Tensão Urbana')

navegador.quit()
