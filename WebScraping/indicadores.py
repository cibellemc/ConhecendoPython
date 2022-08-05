import pandas
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")


def atualiza_html(tempo_sleep):
    sleep(tempo_sleep)
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    return conteudo_web


def conta_options(tempo_sleep, nome_elemento):
    web_atualizado = atualiza_html(tempo_sleep)
    lista_E = web_atualizado.find('select', {'id': f'frm{nome_elemento}'})

    qtd_E = int(len(lista_E) / 2)
    return qtd_E


def seleciona(nome_elemento, nome_contador):
    selecao = Select(navegador.find_element(f'xpath', f'//*[@id="frm{nome_elemento}"]'))
    selecao.select_by_index(nome_contador)


def cria_lista(nome_elemento):
    web_atualizado = atualiza_html(2)
    find_E = web_atualizado.find('select', {'id': f'frm{nome_elemento}'}).get_text()
    E = find_E.split('\n')
    print(E[2:-1])


lista_estados = cria_lista('Estados')

for e in range(1, 28):
    seleciona('Estados', e)

    qtd_municipios = conta_options(2.5, 'Municipios')
    # print(qtd_municipios)
    lista_municipios = cria_lista('Municipios')

    for m in range(1, qtd_municipios):
        seleciona('Municipios', m)

        qtd_anos = conta_options(1, 'Anos')
        # print(qtd_anos)
        lista_anos = cria_lista('Anos')

        for a in range(1, qtd_anos):
            seleciona('Anos', a)

            qtd_conjuntos = conta_options(1, 'Conjuntos')
            # print(qtd_conjuntos)
            lista_conjuntos = cria_lista('Conjuntos')

            for c in range(1, qtd_conjuntos):
                seleciona('Conjuntos', c)

                pd = pandas.DataFrame({'Estado': lista_estados[e+1],
                                       'Município': lista_municipios[m+1],
                                       'Ano': lista_anos[a+1],
                                       'Conjunto': lista_conjuntos[c+1]})
    print(pd)
    print('\n')

navegador.quit()
