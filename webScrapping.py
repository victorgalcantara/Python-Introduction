# -*- coding: utf-8 -*-
"""
Ex. Web Scrapping
Created on Thu Aug 11 12:27:29 2022
@author: VictorGabriel
"""

# 0. Packages and setup
# =============================================================================
# pip install html5lib
# pip install BeautifulSoup
# pip install lxml
# pip install requests
# =============================================================================

import pandas as pd
import os
import html5lib
from bs4 import BeautifulSoup as soup
import lxml
import requests

# Verificando pacotes necessários
!pip show pandas html5lib beautifulsoup4 lxml requests

os.getcwd()
os.chdir("G:/Meu Drive/00 data/SAEB/2019/DADOS/")

# URL: endereço da página HTML em que vamos extrair os dados
url = "https://pt.wikipedia.org/wiki/Lista_de_conflitos_envolvendo_o_Brasil"
# =============================================================================
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) \
                          AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/44.0.2403.157 Safari/537.36'})
  
# creating request object
req = requests.get(url, headers={"Content-Type":"text"})
req.content

# Criando objeto soup
url = soup(req.content, features="html.parser")

# you get a more organised content
url

t = soup.find_all(url,class_="mw-headline") 
type(t)
len(t)
soup.get_text(t[1])

# pandas read html: lendo tabelas na página HTML
tabelas = pd.read_html(io=url, # endereço da página/link
                  flavor='bs4',                   # the parsing engine
                  attrs = {'class': 'wikitable'}) # atributos de local. html

# observando os dados
type(tabelas) # Listas com as tabelas
len(tabelas)  # Qtd. de listas/tabelas extraídas da página

type(tabelas[0])   # tabelas estruturadas como data.frames
tabelas[0].shape   # Qtd. linhas x colunas
tabelas[0].columns # Colunas
tabelas[0].info()  # Estrutura variáveis

# Exportando tabelas
tabelas[0].to_csv(os.path.join("DataFiles","guerras1P.csv"),index=False)
tabelas[1].to_csv(os.path.join("DataFiles","guerras2P.csv"),index=False)
tabelas[2].to_csv(os.path.join("DataFiles","guerras3P.csv"),index=False)