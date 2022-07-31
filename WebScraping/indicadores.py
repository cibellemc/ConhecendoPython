from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select

# define navegador e entra na página
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

# .page_source pega o conteudo html
conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')

# .find() pode conter só o nome da tag, retornando a primeira que encontrar
# .find() pode ter um combo, com a tag e um dicionario (atributo e valor)
# exemplo: soup.find('div', {'class': 'footer'})

# pega os estados na tag select
lista_estados = conteudo_web.find('select', {'id': 'frmEstados'})

# encontra a tag <option> dentro dos estados da <select>
itens_lista_estados = lista_estados.find_all('option')

# na lista de estados, a partir da opcção 1 (o 0 é o "Selecione um estado"), vai printar o atributo value que contem a
# sigla do estado. Depois,  vai selecionar pra habilitar a opção de municipio
for nome_estado in itens_lista_estados[1:]:
    print(nome_estado['value'])
    selecao_estado = Select(navegador.find_element('xpath', '//*[@id="frmEstados"]'))
    selecao_estado.select_by_index(1)
    # seleciona o estado, para poder habilitar a opção

    selecao_municipio = Select(navegador.find_element('xpath', '//*[@id="frmMunicipios"]'))
    selecao_municipio.select_by_index(0)
    sleep(2)

    lista_municipios = conteudo_web.find('select', {'id': 'frmMunicipios'})
    # itens_lista_municipios = lista_municipios.find_all('option')
    print(lista_municipios.prettify())

    """for nome_municipio in lista_municipios:
        print(nome_municipio['value'])"""

navegador.quit()
