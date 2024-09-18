from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './exchange_rate.csv'

# função de registro das etapas do projeto

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # obtém registro de data e hora atual
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')


def extract(url, table_attribs):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    tables = data.find_all('tbody')
    

    # Checando se há tabelas na página da web
    if not tables:
        print("No tables found in the HTML.")
        return pd.DataFrame()  # Retorna um dataframe vazio

    rows = tables[2].find_all('tr')

    df = pd.DataFrame()  # Inicializando um data frame vazio

    for count, row in enumerate(rows[1:11], 1):  # Pula a linha de cabeçalho e extrai as 10 próximas linhas 
        cols = row.find_all('td')
        if len(cols) >= 0: 
            data_dict = {
                table_attribs[0]: cols[1].text.strip(),
                table_attribs[1]: float(cols[2].text.strip().replace(',','')) # Converte string type para float
            }
            df = pd.concat([df, pd.DataFrame(data_dict, index=[0])], ignore_index=True)

    return df

    