import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random

import sys

sys.stdout = open("log.txt", "w")
sys.stderr = open("errori.txt", "w")

TOKEN = "8636760212:AAFVsUGLoY3X1cbrdERWCo6ugpfTYxy9OYQ"
CHAT_ID = "5127739968"
MAPPE_DESIDERATE = ["_666", "_interference", "_axiom", "_tendies", "_demise", "_4am", "_nyx", "_sanctuary","_highlands","_quickie"]
notificate = []

def invia_telegram(messaggio):
    import requests
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': messaggio}
    requests.get(url, params=params)

def controlla_mappe():
    global notificate
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        driver.get("https://ksf.surf/connect")
        time.sleep(10) 
        
        contenuto_pagina = driver.page_source.lower()
        

        print("--- Analisi pagina in corso ---")
        
        mappe_trovate_ora = []
        for m in MAPPE_DESIDERATE:
            if m.lower() in contenuto_pagina:
                print(f"DEBUG: Mappa {m} TROVATA nel codice HTML")
                mappe_trovate_ora.append(m)
                if m not in notificate:
                    invia_telegram(f" Map {m} found on KSF!")
                    notificate.append(m)
            else:
       
                print(f"DEBUG: Mappa {m} NON trovata")
        
        notificate = [m for m in notificate if m in mappe_trovate_ora]
        
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        driver.quit()

invia_telegram("Bot enabled correctly")
while True:
    controlla_mappe()
    time.sleep(random.randint(50, 70))