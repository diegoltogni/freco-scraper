# Freco Scraper

## O que faz
O scraper processa o arquivo .xlsx com uma lista de URLs e adiciona o resultado no arquivo

## Como usar
Antes de qualquer coisa instale os pacotes python necessarios:

```
pip install requests
pip install beautifulsoup4
pip install pandas
```

Depois edite o arquivo `scraper.py` e mude de 
```python
file_path = 'docs/freco.xlsx'
```
para o endereço do arquivo que vc quer executar. Por exemplo, caso o arquivo python e o arquivo excel estejam na mesma pasta:
```python
file_path = 'links.xlsx'
```

Execute o arquivo rodando `python scraper.py`