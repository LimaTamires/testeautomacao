''' 1 exmemplo - utilizando wget
pip install wget, no terminal
1º exemplo: baixar direto do link do arquivo
'''
import wget

link = #link do site para fazer o dowload
wget.download(link, 'nomedoarquivo.extençãoparasersalvo (pdf, img, svg, etc)')

'''
2º exemplo: baixar a partir do site usando selenuim 
1 - instalar selenium no cmd anaconda
2 - instalar webdriver-manager no cmd anaconda (verificar se o anaconda está instalado)

passo 1: entrar na URL desejada
#passo 2 

webdriver do chrome -> chromedriver
webdriver do firefox -> geckodriver'''

#inicio
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #padrao para selenium - Para uso de chrome
from selenium.webdriver.chrome.service import service #executará o chromewebdrivermanager

servico = Service(ChromeDriverManager().install())

navegador = webdriver.chrome(service=servico)

#passo 1: entrar na URL desejada

navegador.get('url') #https etc, link completo

#passo 2: preenchher nome etc
navegador.findelement('xpath', '//*[@id="workbench.parts.editor"]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div[3]/div[2]').click()
# como encontrar o xpath = ctrl+shif+i > copiar > copiarxpath 
# .send.keys('texto') = usado para preencher o campo 
# .click() = usado para clicar no elemento

#-------------------------------------------------------------------------------
''' compactar aquivos'''
from zipfile import Zipfile

with ZipFile('nome_arquivo.zip', 'w') as zip:
     #write
    zip.write('nomedoarquivo1.extensão *(pdf, img, svg)')
    zip.write('nomedoarquivo2.extensão *(pdf, img, svg)')

''' No terminal: python nomedoarquivo (executar o arquivo para criar o zip)'''

'''Descompactar Arquivos'''
#(read)
with ZipFile('nomedoarquivo_zipado.zip', 'r') as zip:
    zip.extractall('''nome da pasta, se quiser extrair para outra''')
    zip.extract('nomedoarquivo', 'nome da pasta') #extrai somente o arquivo indicado no parametro