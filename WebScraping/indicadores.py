from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")


def atualiza_html_e_conta_options(tempo_sleep, nome_elemento):
    sleep(tempo_sleep)

    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    lista_E = conteudo_web.find('select', {'id': f'frm{nome_elemento}'})

    qtd_E = int(len(lista_E) / 2)
    return qtd_E


def seleciona_e_mostra_options(nome_elemento, nome_contador):
    selecao = Select(navegador.find_element(f'xpath', f'//*[@id="frm{nome_elemento}"]'))
    selecao.select_by_index(nome_contador)

    nomeE = navegador.find_element('xpath', f'//*[@id="frm{nome_elemento}"]/option[{nome_contador + 1}]')
    print(nomeE.text)


for e in range(1, 28):
    seleciona_e_mostra_options('Estados', e)

    qtd_municipios = atualiza_html_e_conta_options(2.5, 'Municipios')
    print(qtd_municipios)

    for m in range(1, qtd_municipios):
        seleciona_e_mostra_options('Municipios', m)

        qtd_anos = atualiza_html_e_conta_options(1, 'Anos')
        print(qtd_anos)

        for a in range(1, qtd_anos):
            seleciona_e_mostra_options('Anos', a)

            qtd_conjuntos = atualiza_html_e_conta_options(1, 'Conjuntos')
            print(qtd_conjuntos)

            for c in range(1, qtd_conjuntos):
                seleciona_e_mostra_options('Conjuntos', c)

    print('\n')

navegador.quit()
