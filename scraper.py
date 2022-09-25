import requests
from bs4 import BeautifulSoup
import pandas as pd

def getInfoFromURL(url):
    page = requests.get(url)
    parsed = BeautifulSoup(page.content, "html.parser")
    atributos = {'class': 'row'}
    respostas = parsed.find_all('div',attrs=atributos)
    return respostas

file_path = 'docs/freco.xlsx'
df = pd.read_excel(file_path)

df['page_respostas'] = df['LINKS'].apply(getInfoFromURL)
df.to_excel(file_path, index=False)
