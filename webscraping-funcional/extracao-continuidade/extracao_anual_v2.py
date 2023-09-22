import random
from datetime import date
from time import sleep
import ibge.localidades
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# abre o navegador navegador
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

wait = WebDriverWait(navegador, 10)

# pega os estados da api do ibge é coloca em ordem alfabética
lista_estados = sorted(ibge.localidades.Estados().getNome())

# coloca o vetor em upper case
lista_estados = list(map(lambda x: x.upper(), lista_estados))

lista_capitais = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", 'FORTALEZA', "BRASÍLIA", "VITÓRIA", 'GOIÂNIA',"SÃO LUÍS", "CUIABÁ", 'CAMPO GRANDE', 'BELO HORIZONTE', 'CURITIBA', 'JOÃO PESSOA', 'BELÉM','RECIFE',
'TERESINA', 'NATAL','PORTO ALEGRE', 'RIO DE JANEIRO', 'PORTO VELHO', 'BOA VISTA', 'FLORIANÓPOLIS',
'ARACAJU','SÃO PAULO', 'PALMAS']

ids_gerados = []
linhas_tabela = []
cod_conjuntos = []

df_urb = pd.DataFrame()
df_rur = pd.DataFrame()

log = 'log_' + str(date.today()) + '.txt'
log = open(log, 'w')
log.write('\n')

def seleciona_elementos(nome_unidade, nome_procurado):

    # quando for sp bota 1.5
    sleep(0.5)
    
    # o select só funciona com tag select, entaão seleciona a tag que contém as opcões de estados/municípios
    selecao = Select(navegador.find_element(By.XPATH, f'//*[@id="frm{nome_unidade}"]'))
    
    # procura na página a option com o nome do estado/município
    # se for estado, é contains porque é AC - ACRE
    # se for o resto, correspondência exata
    if nome_unidade == "Estados":
        busca = navegador.find_element(By.XPATH, f'//option[contains(text(),"{nome_procurado}")]')
    else:
        busca = navegador.find_element(By.XPATH, f'//option[normalize-space()="{nome_procurado}"]')
        
    # seleciona (dentro da tag select) onde o texto é o encontrado na busca
    selecao.select_by_visible_text(busca.text)


def atualiza_html_e_conta_options(tempo_sleep, nome_elemento):
    sleep(tempo_sleep)

    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
    lista_e = conteudo_web.find('select', {'id': f'frm{nome_elemento}'})

    # conta abertura e fechamento de <option>, ficando valor dobrado
    return int(len(lista_e) / 2)


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
    sleep(0.5)

    return df


def gerar_id():
    id_aleatorio = random.randint(0, 100)

    if id_aleatorio in ids_gerados:
        while id_aleatorio in ids_gerados:
            id_aleatorio = random.randint(0, 100)

    ids_gerados.append(id_aleatorio)
    return id_aleatorio


for e in range(25, 26):
    # só vai procurar um estado, um município e um ano, dentro disso, vários conjuntos
    try:
        seleciona_elementos("Estados", lista_estados[e])
        sleep(1)

        seleciona_elementos("Municipios", lista_capitais[e])
        sleep(1)

        seleciona_elementos("Anos", 2023)
        qtd_conjuntos = atualiza_html_e_conta_options(0.5, 'Conjuntos')
        sleep(1)

        # se colocar a exceção aqui ele reclama que "qtd_conjuntos não está definida"

        for c in range(2, qtd_conjuntos + 1):
            tentativa = 0

            try:
                for tentativas in range(1, 4):
                    tentativa = tentativas
                    # ['', 'Selecione um Conjunto Elétrico', 'SÃO FRANCISCO', 'TANGARÁ', 'TAQUARI', '']

                    lista_conjuntos = cria_lista('Conjuntos')
                    seleciona_elementos('Conjuntos', lista_conjuntos[c])

                    # captura o código do conjunto com base no texto visível
                    conteudo_web = BeautifulSoup(navegador.page_source, 'html.parser')
                    option_element = conteudo_web.find('option', text=f"{lista_conjuntos[c]}")
                    value = option_element['value']
                    cod_conjuntos.append(value)
                    
                    df1 = tables(0)
                    df2 = tables(1)

                    df_urb = df_urb.append(df1, ignore_index=True)
                    df_rur = df_rur.append(df2, ignore_index=True)

                    linhas_tabela.append([lista_estados[e], lista_capitais[e], 2023, value])
                    log.write(str(f'OK: tentativa {tentativa} - {lista_conjuntos[c]}/{lista_estados[e]}\n'))
                    print(f'OK: tentativa {tentativa} - {lista_conjuntos[c]}/{lista_estados[e]}')
                    break

            except:
                if tentativa == 3:
                    print(str(f'Erro: {lista_capitais[e]}/{lista_estados[e]}'))
                    log.write(str(f'Erro: {lista_capitais[e]}/{lista_estados[e]}'))
                    pass

    except:
        print(str(f'Erro: {lista_estados[e]}'))
        log.write(str(f'Erro: tentativa {lista_estados[e]}'))
        pass

# precisa colocar para que ele escreva
log.close()

# se for de um ano com todas as informações
# df_urb.columns = ['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC T', 'DIC M', 'FIC A', 'FIC T', 'FIC M', 'DMCI', 'DICRI']
# df_rur.columns = ['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC T', 'DIC M', 'FIC A', 'FIC T', 'FIC M', 'DMCI', 'DICRI']

# ano novo
df_urb.columns = ['Conjunto', 'DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']

df_urb[['DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']] = \
df_urb[['DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']].apply(pd.to_numeric)

df_estmunano = pd.DataFrame(linhas_tabela, columns=['Estado', 'Município', 'Ano', 'Cod Conjunto'])

m = pd.merge(df_estmunano, df_urb, right_index=True, left_index=True, how='outer')

with pd.ExcelWriter('limite_conjuntos_' + str(gerar_id()) + '.xlsx') as writer:
    m.to_excel(writer, sheet_name='BT Urb', index=False)

navegador.quit()
