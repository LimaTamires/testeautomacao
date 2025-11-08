import wget
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #padrao para selenium - Para uso de chrome
from selenium.webdriver.chrome.service import Service #executará o chromewebdrivermanager
from selenium.webdriver.chrome.options import Options #executará o chromewebdrivermanager
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)

def link_para_baixar(resp):
    link_element = resp.find_element(By.ID, 'base')
    url_copiada = link_element.get_attribute('href')
    wget.download(url_copiada, 'download.pdf')

#passo 1: entrar na URL desejada
#xpath = //tag[@atributo='valor']
navegador.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos') #https etc, link completo

#ACEITAR COOKIES
navegador.find_element('xpath','/html/body/div[5]/div/div/div/div/div[2]/button[3]').click()

#anexo1
anexo1 = navegador.find_element('xpath','//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]').click()
link_para_baixar(anexo1)


'''
#anexo2
navegador.find_element('xpath','//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a').click()
'''


# como encontrar o xpath = ctrl+shif+i > copiar > copiarxpath 
# .send.keys('texto') = usado para preencher o campo 
# .click() = usado para clicar no elemento

#-------------------------------------------------------------------------------
