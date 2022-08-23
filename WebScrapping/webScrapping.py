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
from bs4 import BeautifulSoup as soup
import html5lib
import lxml
import requests

# Verificando pacotes necessários
!pip show pandas html5lib beautifulsoup4 lxml requests

os.getcwd()
os.chdir("G:/Meu Drive/00 GitHub/Python-Introduction")

# URL: endereço da página HTML em que vamos extrair os dados
url = "https://pt.wikipedia.org/wiki/Lista_de_conflitos_envolvendo_o_Brasil"

# Extraindo tabelas da página =================================================
# pandas read html: lendo tabelas na página HTML
tabelas = pd.read_html(io=url,                    # endereço da página/link
                  flavor='bs4',                   # the parsing engine
                  attrs = {'class': 'wikitable'}) # atributos de local. html

# observando os dados
type(tabelas) # Listas com as tabelas
len(tabelas)  # Qtd. de listas/tabelas extraídas da página

type(tabelas[0])   # tabelas estruturadas como data.frames
tabelas[0].shape   # Qtd. linhas x colunas
tabelas[0].columns # Colunas
tabelas[0].info()  # Estrutura variáveis

# Extraindo títulos das tabelas ===============================================
# Não é obrigatório, mas recomendável inserir infos do localhost que fará 
# requisições em "headers"
# HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) \
#                           AppleWebKit/537.36 (KHTML, like Gecko) \
#                           Chrome/44.0.2403.157 Safari/537.36'})
#   

# requisitando a página html (sem definição de header)
req = requests.get(url, headers={"Content-Type":"text"})
req.content

# Criando objeto soup
url = soup(req.content, features="html.parser")
url # mais organizado em soup

# Agora temos a página estruturada em soup, com metadados que facilitam as operações
# métodos: .title, .p, .a etc.
url.title
url.title.string
url.a

# find_all: encontra todas as tags com ou sem filtros
# neste caso, inserimos o filtro por classe
url.find('a')
url.find_all('a')

todas_as_classes = url.find_all(class_="mw-headline") # local dos títulos via inspeção
todas_as_classes
type(todas_as_classes)
len(todas_as_classes)

# get_text() : extrai texto dentro da tag
todas_as_classes[5].text
todas_as_classes[9].text

for i in todas_as_classes: print(i.text)

tabelas[2].head()

# Exportando tabelas ----------------------------------------------------------
tabelas[0].to_csv(os.path.join("data","guerras-america-portuguesa.csv"),index=False)
tabelas[2].to_csv(os.path.join("data","guerras-imperio.csv"),index=False)
tabelas[3].to_csv(os.path.join("data","guerras-republica-velha.csv"),index=False)
