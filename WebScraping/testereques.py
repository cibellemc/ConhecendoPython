import requests
from bs4 import BeautifulSoup
# requests é otimo pra pegar o conteudo, porem entra em conflito pois predisa interagir cdom a pag pra mudar as opçoes
navegador = requests.get("https://www2.aneel.gov.br/aplicacoes_liferay/srd/indqual/default.cfm")
soup = BeautifulSoup(navegador.text, 'html.parser')
# print(soup.prettify())

lista_estados = soup.find('select', {'id': 'frmEstados'})
print(lista_estados.prettify())

lista_municipios = soup.find('select', {'id': 'frmMunicipios'})
print(lista_municipios.prettify())

"""lista_estados = soup.find(id_='frmEstados')
itens_lista_estados = lista_estados.find_all('option')

for nome_estado in itens_lista_estados:
    print(nome_estado.prettify())"""
