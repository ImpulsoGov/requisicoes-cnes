import requests
import pandas as pd

coMun='120001'
coArea='0004'
coEquipe='2096307'
cnes='0257184'

def getData(coMun,coArea,coEquipe,cnes):
    url = "http://cnes.datasus.gov.br/services/estabelecimentos/atendimento/"+coMun+cnes
    
    payload={}
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
      'Connection': 'keep-alive',
      'Referer': 'http://cnes.datasus.gov.br/pages/estabelecimentos/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    return res
    

data = getData(coMun,coArea,coEquipe,cnes)
