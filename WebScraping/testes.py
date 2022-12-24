from time import sleep
import ibge.localidades
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

# pega os estados da api do ibge é coloca em ordem alfabética
lista_estados = sorted(ibge.localidades.Estados().getNome())

# coloca o vetor em upper case
lista_estados = list(map(lambda x: x.upper(), lista_estados))

lista_capitais = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", 'FORTALEZA', "BRASÍLIA", "VITÓRIA", 'GOIÂNIA',
                  "SÃO LUÍS", "CUIABÁ", 'CAMPO GRANDE', 'BELO HORIZONTE', 'BELÉM', 'JOÃO PESSOA', 'CURITIBA', 'RECIFE',
                  'TERESINA', 'RIO DE JANEIRO', 'NATAL', 'PORTO ALEGRE', 'PORTO VELHO', 'BOA VISTA', 'FLORIANÓPOLIS',
                  'SÃO PAULO', 'ARACAJU', 'PALMAS']

lista_anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


def seleciona_elementos(nome_unidade, nome_procurado):
    # o select só funciona com tag select, entaão seleciona a tag que contém as opcões de estados/municípios
    selecao = Select(navegador.find_element(By.XPATH, f'//*[@id="frm{nome_unidade}"]'))

    # procura na página a option com o nome do estado/município
    busca = navegador.find_element(By.XPATH, f'//option[contains(text(),"{nome_procurado}")]')

    # seleciona (dentro da tag select) onde o texto é o encontrado na busca
    selecao.select_by_visible_text(busca.text)


for e in range(0, 27):
    try:
        seleciona_elementos("Estados", lista_estados[e])
        sleep(1)
        seleciona_elementos("Municipios", lista_capitais[e])
        sleep(1)
        for a in range(0, 14):
            seleciona_elementos("Anos", lista_anos[a])
    except:
        print(f"Rápido demais - {lista_estados[e]}, {lista_capitais[e]}, {lista_anos[a]}")
        pass