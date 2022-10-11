from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dólar")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Ao identificar o xpath é importante que o escreva dentro de aspas simples, pois dentro do código as vezes pode haver aspas duplas, o que iria interferir na leitura do código
cotacao_dolar = (navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value"))
navegador.quit
navegador.get('https://www.google.com.br/')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = (navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value"))
navegador.quit
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = (navegador.find_element('xpath','//*[@id="comercial"]').get_attribute("value"))
navegador.quit
print (cotacao_dolar)
print (cotacao_euro)
print (cotacao_ouro)
import pandas as pd
tabela = pd.read_excel('Produtos.xlsx')
print(tabela)