from ast import Or
from cgitb import text
from mimetypes import init
from multiprocessing.connection import wait
import os.path
from statistics import mode
from datetime import datetime
from numpy import append, obj2sctype
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

class newBot:
    
    def __init__(self, nome_bot):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.chrome_options.add_argument('--disable-software-rasterizer')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        #---------------LEMBRE-SE DE ALTERAR O CAMINHO DO WEBDRIVER-----------------
        self.driver = webdriver.Chrome(executable_path=r"C:\bin\chromedriver.exe")

    def extract(self):
        #----------DEFINIR QUANTIDADE DE IDS EXTRAÍDOS --------------
        #-Média de 1.8s por id
        qtdIDS = 200

        #------- DEFINIR CICLO DE SAVE --------
        #(Salvar no arquivo a cada X ids)
        qtdSave = 20

        #-----DEFINIR ID INICIAL CASO NÃO EXISTA NENHUM NO DADO CSV (id-1)-----
        lastID = 1953729
        
        if os.path.exists("searates.csv") == False:
            newFile = open("searates.csv", 'w')
            newFile.write('"origem";"destino";"preço";"companhia";"idFrete"\n')
            newFile.close()

        reader = pd.read_csv("searates.csv", sep=";", encoding='latin-1')
        readerLines = len(reader.index)

        if readerLines != 0:
            lastID = reader.loc[readerLines-1, "idFrete"]

        site = 'https://www.searates.com/freight/?id='
        wait = WebDriverWait(self.driver, 10)
        data = pd.DataFrame(columns=['origem', 'destino', 'preço', 'companhia', 'idFrete'])
        
        for i in range(int(qtdIDS/qtdSave)):

            for j in range(qtdSave):
                lastID+=1
                self.driver.get(site+str(lastID))
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[2]/button/span[1]')))
                
                price = self.driver.find_element(By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[2]/button/span[1]').text
                company = self.driver.find_element(By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[1]/div[1]/div[2]').text
                origin = self.driver.find_element(By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[1]/div[2]/div[1]/div[1]').text
                destiny = self.driver.find_element(By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[1]/div[2]/div[1]/div[2]').text
                vesselId = self.driver.find_element(By.XPATH, '//*[@id="marketplace"]/main/div/div[2]/div[2]/div[1]/div[1]/article/div[1]/div[2]/div/div[3]/div[2]/span').text

                data.at[j,'origem'] = origin
                data.at[j,'destino'] = destiny
                data.at[j,'preço']=price
                data.at[j,'companhia']=company
                data.at[j,'idFrete']=vesselId

            data.to_csv("searates.csv", sep=";", mode='a', header=False, index=False)

        self.driver.close()