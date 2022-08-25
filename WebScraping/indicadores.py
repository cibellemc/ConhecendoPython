import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

estmunanoconj = []


def atualiza_html_e_conta_options(tempo_sleep, nome_elemento):
    sleep(tempo_sleep)

    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    lista_E = conteudo_web.find('select', {'id': f'frm{nome_elemento}'})

    return int(len(lista_E) / 2)


def seleciona_elemento(nome_elemento, nome_contador):
    selecao = Select(navegador.find_element('xpath', f'//*[@id="frm{nome_elemento}"]'))
    selecao.select_by_index(nome_contador)


def cria_lista(nome_elemento):
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    find_el = conteudo_web.find("select", {"id": f"frm{nome_elemento}"}).get_text()
    return find_el.split('\n')


def tables(indice_table):
    sleep(2)
    web = BeautifulSoup(navegador.page_source, 'html.parser')
    tabelas = web.find('div', {'id': 'resposta'}).find_all('tr', {'class': 'res'})

    if indice_table == 1:
        tabela1 = tabelas[0].text.strip().split("\n")
    else:
        tabela1 = tabelas[1].text.strip().split("\n")

    df1 = pd.DataFrame(tabela1).replace(',', '.', regex=True).transpose()
    sleep(2)

    return df1


for e in range(1, 2):
    seleciona_elemento('Estados', e)
    lista_estados = cria_lista('Estados')
    qtd_municipios = atualiza_html_e_conta_options(2.5, 'Municipios')

    for m in range(1, 2):
        seleciona_elemento('Municipios', m)
        lista_municipios = cria_lista('Municipios')
        qtd_anos = atualiza_html_e_conta_options(1, 'Anos')

        for a in range(1, 2):
            seleciona_elemento('Anos', a)
            lista_anos = cria_lista('Anos')
            qtd_conjuntos = atualiza_html_e_conta_options(1.5, 'Conjuntos')

            for c in range(1, 2):
                seleciona_elemento('Conjuntos', c)

                df1 = tables(1)
                print(df1)

                df2 = tables(2)
                print(df2)


navegador.quit()
