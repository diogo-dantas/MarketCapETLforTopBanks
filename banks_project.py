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

def transform(df):
    exchange_df = pd.read_csv(csv_path) # le a taxa de câmbio do arquivo csv
    exchange_rate = exchange_df.set_index('Currency').to_dict()['Rate'] # converte em dicionário 
    exchange_rate = {k: float(v) for k, v in exchange_rate.items()} # cast valores para type float

    #converte os valores de acordo com a taxa de câmbio
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    return df

def load_to_csv(df, csv_path): #armazena o dataframe em csv
    df.to_csv('./Largest_banks_data.csv')

def load_to_db(df, sql_connection, table_name): #armazena os dados no banco de dados
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)