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

    qtd_E = int(len(lista_E) / 2)
    return qtd_E


def seleciona_elemento(nome_elemento, nome_contador):
    selecao = Select(navegador.find_element(f'xpath', f'//*[@id="frm{nome_elemento}"]'))
    selecao.select_by_index(nome_contador)


def cria_lista(nome_elemento):
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    find_es = conteudo_web.find("select", {"id": f"frm{nome_elemento}"}).get_text()
    estados = find_es.split('\n')
    return estados


for e in range(1, 28):
    seleciona_elemento('Estados', e)

    lista_estados = cria_lista('Estados')

    qtd_municipios = atualiza_html_e_conta_options(2.5, 'Municipios')
    # print(qtd_municipios)

    for m in range(1, qtd_municipios):
        seleciona_elemento('Municipios', m)

        lista_municipios = cria_lista('Municipios')
        # print(lista_municipios[m + 1])

        qtd_anos = atualiza_html_e_conta_options(1, 'Anos')
        # print(qtd_anos)

        for a in range(1, qtd_anos):
            seleciona_elemento('Anos', a)

            # lista_anos = cria_lista('Anos')
            # print(lista_anos[a + 1])

            qtd_conjuntos = atualiza_html_e_conta_options(1.5, 'Conjuntos')
            # print(qtd_conjuntos)

            for c in range(1, qtd_conjuntos):
                seleciona_elemento('Conjuntos', c)

                # lista_conjuntos = cria_lista('Conjuntos')
                # print(lista_conjuntos[c + 1])
                sleep(2)
                web = BeautifulSoup(navegador.page_source, 'html.parser')
                tables = web.find_all('table', {'width': '520px'})
                print(tables)

navegador.quit()
