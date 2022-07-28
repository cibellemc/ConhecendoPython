import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath',
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

# cotacao euro
navegador = webdriver.Chrome()

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath',
                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

# cotacao ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

print(cotacao_ouro)

navegador.quit()
# vem como texto e o separador errado com virgula

tabela = pd.read_excel("Produtos.xlsx", sheet_name=0)
print(tabela)

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
print(tabela["Cotação"])

""".send_keys
.click
.get """