from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

# define navegador e entra na página
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

# se a range começar em 2, mostra no console antes de selecionar
for c in range(1, 10):
    # seleciona o estado, para poder habilitar a opção
    selecao_estado = Select(navegador.find_element('xpath', '//*[@id="frmEstados"]'))
    selecao_estado.select_by_index(c)

    nome_estado = navegador.find_element('xpath', f'//*[@id="frmEstados"]/option[{c+1}]')
    print(nome_estado.text)

    sleep(1)

    # .page_source pega o conteudo html
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')

    # ao verificar o tamanho da lista_municipios dava um valor dobrado, provavelmente contando inicio e
    # fim de tags, entao dividi por 2, peguei a parte inteira. DF = 5/2 = int(2,5) = 2
    lista_municipios = conteudo_web.find('select', {'id': 'frmMunicipios'})

    qtd_municipios = int(len(lista_municipios)/2)
    print(qtd_municipios)

    for m in range(1, qtd_municipios):
        selecao_municipio = Select(navegador.find_element('xpath', '//*[@id="frmMunicipios"]'))
        selecao_municipio.select_by_index(m)

        nome_municipio = navegador.find_element('xpath', f'//*[@id="frmMunicipios"]/option[{m+1}]')
        print(nome_municipio.text)

navegador.quit()
