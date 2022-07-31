from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

# define navegador e entra na página
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

# se a range começar em 2, mostra no console antes de selecionar
for c in range(1, 28):
    # seleciona o estado, para poder habilitar a opção
    selecao_estado = Select(navegador.find_element('xpath', '//*[@id="frmEstados"]'))
    selecao_estado.select_by_index(c)

    nome_estado = navegador.find_element('xpath', f'//*[@id="frmEstados"]/option[{c+1}]')
    print(nome_estado.text)
    # // *[ @ id = "frmMunicipios"] / option[140]
    # //*[@id="frmMunicipios"]/option[76]

    sleep(1)

    # .page_source pega o conteudo html
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')

    lista_municipios = conteudo_web.find('select', {'id': 'frmMunicipios'})
    qtd_municipios = int(len(lista_municipios)/2) - 1
    print(qtd_municipios)

"""    for m in range(2, qtd_municipios):
        selecao_municipio = Select(navegador.find_element('xpath', '//*[@id="frmMunicipios"]'))
        selecao_municipio.select_by_index(m)

        nome_municipio = navegador.find_element('xpath', f'//*[@id="frmMunicipios"]/option[{m}]')
        print(nome_municipio.text)"""

navegador.quit()
