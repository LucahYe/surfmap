import time
import random
import requests
from bs4 import BeautifulSoup

TOKEN = "8636760212:AAFVsUGLoY3X1cbrdERWCo6ugpfTYxy9OYQ"
CHAT_ID = "5127739968"
MAPPE_DESIDERATE = ["_666", "_interference", "_axiom", "_tendies", "_demise", "_4am", "_nyx", "_sanctuary","_highlands","_quickie","_reverie"]
notificate = []

def invia_telegram(messaggio):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': messaggio}
    try:
        requests.get(url, params=params)
    except Exception as e:
        print(f"Errore invio Telegram: {e}")

def controlla_mappe():
    global notificate
    url = "https://ksf.surf/connect"
    
    try:
        # Scarica la pagina in modo leggero
        headers = {'User-Agent': 'Mozilla/5.0'}
        risposta = requests.get(url, headers=headers, timeout=15)
        
        if risposta.status_code == 200:
            contenuto = risposta.text.lower()
            mappe_trovate_ora = []
            
            for m in MAPPE_DESIDERATE:
                if m.lower() in contenuto:
                    mappe_trovate_ora.append(m)
                    if m not in notificate:
                        invia_telegram(f" Map surf{m} found on KSF!")
                        notificate.append(m)
            
            notificate = [m for m in notificate if m in mappe_trovate_ora]
        else:
            print(f"Errore connessione: {risposta.status_code}")
            
    except Exception as e:
        print(f"Errore scraping: {e}")

# Avvio
invia_telegram("Bot enabled correctly (Requests mode)")
while True:
    controlla_mappe()
    time.sleep(random.randint(50, 70))
