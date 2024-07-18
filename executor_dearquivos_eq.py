from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Função para esperar até que um novo arquivo apareça no diretório de downloads
def wait_for_downloads(download_dir, timeout=30):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(download_dir):
            if fname.endswith('.crdownload'):  # Arquivo temporário de download do Chrome
                dl_wait = True
        seconds += 1
    return not dl_wait

# Solicita ao usuário para inserir as datas de início e fim
data_inicio = input("Digite a data de início (formato: dd/mm/yyyy): ")
data_fim = input("Digite a data de fim (formato: dd/mm/yyyy): ")

# Configurações do WebDriver
download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': download_dir}
options.add_experimental_option('prefs', prefs)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

try: 
    # Abre a página de login
    navegador.get('https://portal.professor24h.com.br/#/login')

    # Insere e-mail e senha
    email_input = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    email_input.send_keys('instituicao@escrevendonaquarentena.org')

    senha_input = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    senha_input.send_keys('EQinstituicao2022')

    entrar_input = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/button')))
    entrar_input.click()

    # Espera até concluir o login
    WebDriverWait(navegador, 10).until(
        EC.url_to_be('https://portal.professor24h.com.br/#/escola/dashboard'))
    
    time.sleep(5)

    # Navega para a página de redações
    navlink_redacoes = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/ul/li[5]/a')))
    navlink_redacoes.click()

    WebDriverWait(navegador, 10).until(
        EC.url_to_be('https://portal.professor24h.com.br/#/redacoes'))

    # Insere as datas de início e fim
    click_datas = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[1]/div/div/form/div/div[1]/div/div[2]/div/span/span/span')))
    click_datas.click()


    data_fim_input = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/input')))
    data_fim_input.send_keys(data_fim)

    # Realiza a busca
    busca = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[1]/div/div/form/div/div[2]/button')))
    busca.click()

    # Seleciona todas as redações
    check = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div[3]/div[1]/div[3]/div/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/label/span[1]/input')))
    check.click()

    # Exporta para CSV
    botao_csv = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/button')))
    botao_csv.click()

    baixar_csv = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/ul/li[3]/a')))
    baixar_csv.click()

    # Espera até que o arquivo seja baixado
    if wait_for_downloads(download_dir):
        print("Arquivo baixado com sucesso! :)")
    else:
        print("Tempo de espera esgotado. O arquivo não foi baixado. :(")

    time.sleep(20)

except Exception as e: 
    print('Erro:', e)

finally:
    navegador.quit()
