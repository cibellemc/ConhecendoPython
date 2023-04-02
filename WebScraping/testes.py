from time import sleep
import time
import ibge.localidades
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

# abre o navegador navegador
navegador = webdriver.Chrome()
navegador.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")

wait = WebDriverWait(navegador, 10)

# pega os estados da api do ibge é coloca em ordem alfabética
lista_estados = sorted(ibge.localidades.Estados().getNome())
# Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Paraná', 'Paraíba', 'Pará', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rio de Janeiro', 'Rondônia', 'Roraima', 'Santa Catarina', 'Sergipe', 'São Paulo', 'Tocantins'

# coloca o vetor em upper case
lista_estados = list(map(lambda x: x.upper(), lista_estados))

lista_capitais = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", 'FORTALEZA', "BRASÍLIA", "VITÓRIA", 'GOIÂNIA', "SÃO LUÍS", "CUIABÁ", 'CAMPO GRANDE', 'BELO HORIZONTE', 'CURITIBA','JOÃO PESSOA', 'BELÉM','RECIFE','TERESINA',  'NATAL', 'PORTO ALEGRE', 'RIO DE JANEIRO',  'PORTO VELHO', 'BOA VISTA', 'FLORIANÓPOLIS','ARACAJU','SÃO PAULO',  'PALMAS']

data = pd.DataFrame()
tabela_rur = pd.DataFrame()
tabela_urb = pd.DataFrame()

def seleciona_elementos(nome_unidade, nome_procurado):
    sleep(0.5)
    # o select só funciona com tag select, entaão seleciona a tag que contém as opcões de estados/municípios
    selecao = Select(navegador.find_element(By.XPATH, f'//*[@id="frm{nome_unidade}"]'))

    # procura na página a option com o nome do estado/município
    busca = navegador.find_element(By.XPATH, f'//option[contains(text(),"{nome_procurado}")]')

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

# função p/ transformar em tabela
def tabela(indice):
    sleep(0.5)
    element = navegador.find_element(By.XPATH, '//*[@id="resposta"]/table[{}]'.format(indice))
    
    html_element = element.get_attribute('outerHTML')

    df_aux = pd.read_html(html_element.replace(',', '.'))
    df_aux[0].drop([0,1], inplace=True)

    return df_aux[0]
 
tempo_inicial = time.time() # em segundos

for e in range(0, 27):
    for tentativa in range(3):
        try:
        # só vai procurar um estado, um município e um ano, dentro disso, vários conjuntos
            seleciona_elementos("Estados", lista_estados[e])
            seleciona_elementos("Municipios", lista_capitais[e])
            seleciona_elementos("Anos", 2023)
            qtd_conjuntos = atualiza_html_e_conta_options(0.5, 'Conjuntos')

            # se colocar a exceção aqui ele reclama que "qtd_conjuntos não está definida"
            for c in range(2, qtd_conjuntos + 1):

                lista_conjuntos = cria_lista('Conjuntos')
                seleciona_elementos('Conjuntos', lista_conjuntos[c])

                tabela_urb = tabela_urb.append(tabela(1))
                tabela_rur = tabela_urb.append(tabela(2))

        except:
                if tentativa == 3:
                    print(str(f'Erro: {tentativa}º tentativa - {lista_capitais[e]}/{lista_estados[e]}'))
                pass

def exportar_tabelas():
    if(tabela_urb.shape[1]) > 7:
        tabela_urb.columns=['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC T', 'DIC M', 'FIC A', 'FIC T', 'FIC M', 'DMCI', 'DICRI']
        tabela_rur.columns=['Conjunto', 'DEC', 'FEC', 'DIC A', 'DIC T', 'DIC M', 'FIC A', 'FIC T', 'FIC M', 'DMCI', 'DICRI']
    else :
        tabela_urb.columns = ['Conjunto', 'DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']
        tabela_rur.columns = ['Conjunto', 'DEC', 'FEC', 'DIC M', 'FIC M', 'DMCI', 'DICRI']

    with pd.ExcelWriter('limite_conjuntos1234.xlsx') as writer:
        tabela_urb.to_excel(writer, sheet_name='BT Urb', index=False)
        tabela_rur.to_excel(writer, sheet_name='BT Rur', index=False)

exportar_tabelas()
tempo_final = time.time() # em segundos
print(f"\n--- Tempo de busca ---\nAproximadamente {round(tempo_final - tempo_inicial,1)} segundos")
navegador.quit()
