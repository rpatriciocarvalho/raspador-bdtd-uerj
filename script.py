from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse

# Apenas para trabalho local
import os
diretorio = os.getcwd()

# Lista de defesas pós-graduacao em Física
#http://www.bdtd.uerj.br/tde_busca/resultado-tdes-prog.php?ver=34&programa=34&ano_inicio=&mes_inicio=&mes_fim=&ano_fim=2018&grau=Todos

# Detalhes de uma defesa
#http://www.bdtd.uerj.br/tde_busca/processaPesquisa.php?listaDetalhes%5B%5D=8962&processar=Processar

pagina = urlopen('file:///' + diretorio + '/pos.html')
sopa = BeautifulSoup(pagina, 'html.parser')

tabela = sopa.find(class_='txt')
a = tabela.find_all('a')
del(a[0])

lista_id = []

for link in a:
    url = urlparse(link.get('href'))
    lista_id.append(url.query.split('=')[-1])

print(lista_id)

## -- IMPLEMENTAR -- ##
# Detalhe para cada defesa
#detalhes = urlopen('file:///' + diretorio + '/detalhe.html')
#sopa_detalhes = BeautifulSoup(detalhes, 'html.parser')

#detalhes = sopa_detalhes.find_all(class_='BuscaTxt')

#print(detalhes)