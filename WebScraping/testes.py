from time import sleep
import ibge.localidades
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By

# abre o navegador navegador
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

wait = WebDriverWait(navegador, 10)

# pega os estados da api do ibge é coloca em ordem alfabética
lista_estados = sorted(ibge.localidades.Estados().getNome())

# coloca o vetor em upper case
lista_estados = list(map(lambda x: x.upper(), lista_estados))

lista_capitais = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", 'FORTALEZA', "BRASÍLIA", "VITÓRIA", 'GOIÂNIA',
                  "SÃO LUÍS", "CUIABÁ", 'CAMPO GRANDE', 'BELO HORIZONTE', 'BELÉM', 'JOÃO PESSOA', 'CURITIBA', 'RECIFE',
                  'TERESINA', 'RIO DE JANEIRO', 'NATAL', 'PORTO ALEGRE', 'PORTO VELHO', 'BOA VISTA', 'FLORIANÓPOLIS',
                  'SÃO PAULO', 'ARACAJU', 'PALMAS']

lista_anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

dados_tabela = []
linhas_tabela = []

df_urb = pd.DataFrame()
df_rur = pd.DataFrame()


def seleciona_elementos(nome_unidade, nome_procurado):
    # o select só funciona com tag select, entaão seleciona a tag que contém as opcões de estados/municípios
    selecao = Select(navegador.find_element(By.XPATH, f'//*[@id="frm{nome_unidade}"]'))

    # procura na página a option com o nome do estado/município
    busca = navegador.find_element(By.XPATH, f'//option[contains(text(),"{nome_procurado}")]')

    # seleciona (dentro da tag select) onde o texto é o encontrado na busca
    selecao.select_by_visible_text(busca.text)


def atualiza_html_e_conta_options(tempo_sleep, nome_elemento):
    sleep(tempo_sleep)

    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    lista_E = conteudo_web.find('select', {'id': f'frm{nome_elemento}'})

    # conta abertura e fechamento de <option>, ficando valor dobrado
    return int(len(lista_E) / 2)


def cria_lista(nome_elemento):
    # sleep(2)
    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    find_el = conteudo_web.find("select", {"id": f"frm{nome_elemento}"}).get_text()
    return find_el.split('\n')


# caso índice 0 -> bt urb, caso 1 -> bt nao urb
def tables(indice_table):
    # espera até as tabelas estarem na tela
    locator = (By.XPATH, '//*[@id="resposta"]/table[2]')
    wait.until(ec.presence_of_element_located(locator))

    # capta o conteúdo e encontra as option de resposta
    web = BeautifulSoup(navegador.page_source, 'html.parser')
    tabelas = web.find('div', {'id': 'resposta'}).find_all('tr', {'class': 'res'})

    # transforma pra texto em caps lock
    tabela = tabelas[indice_table].text.strip().upper().split("\n")

    # troca , por ponto e bota na horizontal
    df = pd.DataFrame(tabela).replace(',', '.', regex=True).transpose()
    sleep(1)

    return df


for e in range(0, 1):
    try:
        seleciona_elementos("Estados", lista_estados[e])
        sleep(1)
        seleciona_elementos("Municipios", lista_capitais[e])
        sleep(2)

        for a in range(0, 4):
            seleciona_elementos("Anos", lista_anos[a])
            qtd_conjuntos = atualiza_html_e_conta_options(1.5, 'Conjuntos')
            sleep(1)

            # ['', 'Selecione um Conjunto Elétrico', 'SÃO FRANCISCO', 'TANGARÁ', 'TAQUARI', '']
            for c in range(2, qtd_conjuntos + 1):
                lista_conjuntos = cria_lista('Conjuntos')
                seleciona_elementos('Conjuntos', lista_conjuntos[c])

                df1 = tables(0)
                df2 = tables(1)

                df_urb = df_urb.append(df1, ignore_index=True)
                df_rur = df_rur.append(df2, ignore_index=True)

                linhas_tabela.append([lista_estados[e], lista_capitais[e], lista_anos[a]])

    except:
        print("Erro")
        pass

df_urb.columns = ['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC M', 'DIC T', 'FIC A', 'FIC M', 'FIC T', 'DMCI', 'DICRI']
df_rur.columns = ['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC M', 'DIC T', 'FIC A', 'FIC M', 'FIC T', 'DMCI', 'DICRI']

df_estmunanocon = pd.DataFrame(linhas_tabela, columns=['Estado', 'Município', 'Ano'])

m = pd.merge(df_estmunanocon, df_urb.astype(float), right_index=True, left_index=True, how='outer')

m.to_excel("testeconj.xlsx", sheet_name='Baixa Tensão Urbana', index=False)
navegador.quit()
