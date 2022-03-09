from ast import Or
from cgitb import text
from mimetypes import init
from multiprocessing.connection import wait
import os.path
import site
import time
import re
from datetime import datetime
from numpy import obj2sctype
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#---------------LEMBRE-SE DE ALTERAR O CAMINHO DO WEBDRIVER-----------------
driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")


try:
    site = 'https://www.searates.com/services/distances-time/'
    driver.get(site)
    print("hey1")
    wait = WebDriverWait(driver, 10)
    print("hey2")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/button'))) #Espera o site carregar
    print("hey3")
    #driver.send_keys_to_element(By.XPATH)
    originInput = driver.find_element(By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[1]/div/input').send_keys("Santos, BR") #Preenche o campo origem
    print("hey4")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[1]/div/div/div[1]'))) #Espera aparecer o card de origem
    driver.find_element(By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[1]/div/div/div[1]').click() #Clica no card de origem
    print("hey5")
    destinyInput = driver.find_element(By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[2]/div/input').send_keys("Rotterdam, NL")#Preenche o campo destino
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[2]/div/div/div[1]/div/span[2]')))#Espera aparecer o card de destino
    driver.find_element(By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/div[2]/div[2]/div/div/div[1]/div/span[2]').click() #Clica no card de destino

    driver.find_element(By.XPATH, '//*[@id="distance__time-app"]/div/form/div[1]/button').click() #Clica no botão de busca

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="panel"]/div[2]/ul/li[1]/p[2]'))) #Aguarda os resultados
    print("hey6")
    
except:
    print("heye")