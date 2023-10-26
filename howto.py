# flake8: noqa

"""
*WEB SCRAPING COM PYTHON*
========================

O que é Web Scraping?

Web Scraping é uma técnica utilizada para extrair informações de websites. A ideia é transformar a informação disponível em páginas web em dados estruturados para análise posterior.

# --------------------------------------------------------------------------------

Como funciona o Web Scraping?

Basicamente, o web scraping envolve o envio de requisições HTTP para os websites desejados, recebendo as respostas (geralmente em HTML) e, em seguida, analisando esse HTML para extrair as informações desejadas.

# --------------------------------------------------------------------------------

Por que Python para Web Scraping?

Python é uma escolha popular para web scraping devido à sua simplicidade e à vasta gama de bibliotecas disponíveis, como Beautiful Soup, Scrapy e Requests.
Além disso, Python oferece facilidades para o tratamento e análise dos dados coletados, graças a bibliotecas como Pandas e NumPy.

# --------------------------------------------------------------------------------

Utilidade do Web Scraping:

Web scraping é extremamente útil em várias áreas. Por exemplo, um pesquisador pode coletar dados sobre determinados fatores ambientais em diferentes regiões para análise estatística. Empresas podem monitorar os preços dos concorrentes, enquanto jornalistas podem usar web scraping para coletar dados para suas matérias.

# --------------------------------------------------------------------------------

Ferramentas e Fundamentos Necessários:

1. Requests: Biblioteca para enviar requisições HTTP.
2. Beautiful Soup: Biblioteca para analisar o HTML e extrair informações.
3. Scrapy: Framework mais robusto para web scraping.
4. Selenium: Ferramenta para interagir com páginas web que requerem interação com JavaScript.

LEMBRE-SE DE USAR O VIRTUAL ENVIRONMENT!


```bash
  python -m venv venv && source .venv/bin/activate
  pip install requests beautifulsoup4 scrapy pandas openpyxl
```

Bônus (Ferramentas úteis para tratamento e visualização de dados):

1. Pandas: Biblioteca para manipulação e análise de dados.
2. Matplotlib: Biblioteca para criação de gráficos e visualizações de dados.
3. Seaborn: Biblioteca para visualização de dados baseada no Matplotlib.
4. Plotly: Biblioteca para criação de gráficos e visualizações de dados interativos.

# --------------------------------------------------------------------------------

Fun Fact:

Mark Zuckerberg usou web scraping para coletar dados de perfis do Face Book para criar o Facemash, um site que permitia aos usuários votar em qual dos dois perfis era mais atraente.

O nome Beautiful Soup é inspirado em no poema de Lewis Carroll, "Alice no País das Maravilhas", onde a Rainha de Copas diz: "Beautiful Soup, so rich and green, Waiting in a hot tureen!".
O autor da biblioteca, Leonard Richardson, disse que escolheu o nome porque queria algo "bonito" para analisar documentos XML.

# --------------------------------------------------------------------------------

HTTP Básico:

HTTP (Hypertext Transfer Protocol) é o protocolo utilizado para transferir dados pela internet. O HTTP funciona como um protocolo de requisição e resposta entre um cliente e um servidor. Criado por Tim Berners-Lee (também conhecido por TBL ou Cabeção), em 1989.

Requisição HTTP:
Uma requisição HTTP é basicamente uma mensagem enviada pelo cliente (geralmente um navegador) para o servidor, solicitando alguma informação ou ação. As requisições HTTP têm métodos que indicam a ação desejada a ser realizada no recurso especificado. Os mais comuns são GET (para obter dados) e POST (para enviar dados).
Ela retorna um código de status HTTP, que indica se a requisição foi bem sucedida ou não.

Códigos de Status HTTP:
1xx: Informacional (A requisição foi recebida e o processo continua) ex: 100 Continue
2xx: Sucesso (A requisição foi bem sucedida) ex: 200 OK
3xx: Redirecionamento (A requisição foi redirecionada) ex: 301 Moved Permanently
4xx: Erro do Cliente (A requisição não foi bem sucedida) ex: 404 Not Found
5xx: Erro do Servidor (O servidor não conseguiu processar a requisição) ex: 500 Internal Server Error

Exemplo de Requisição HTTP:
GET / HTTP/1.1
Host: www.google.com
Connection: keep-alive
Accept: text/html
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Accept-Encoding: gzip, deflate, br
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7

Exemplo de Resposta HTTP:
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Date: Sun, 01 Aug 2021 18:00:00 GMT
Server: gws
Content-Length: 1558
...etc

# --------------------------------------------------------------------------------

Ciclo de Vida de um Scrape:

1. Enviar uma requisição HTTP para a URL desejada.
2. Receber a resposta HTTP e extrair o HTML.
3. Analisar o HTML e localizar as informações desejadas.
4. Extrair e tratar as informações desejadas do HTML.
5. Armazenar os dados em um arquivo ou banco de dados.

Exemplo:

1. Usa o Requests para enviar uma requisição GET para a URL https://www.example.com.
2. Receber a resposta com o código de status 200 e o HTML.
3. Usar o Beautiful Soup para analisar o HTML.
4. Localizar e extrair o título da página.
5. Armazenar o título em um arquivo ou banco de dados.

# --------------------------------------------------------------------------------

Práticas Recomendadas:

1. Sempre verifique o robots.txt do site antes de fazer o scrape.
- O robots.txt é um arquivo que contém as regras para os crawlers dos sites. Ele indica quais páginas podem ser rastreadas e quais não podem. É uma boa prática verificar o robots.txt antes de fazer o scrape, para evitar problemas legais.
- Exemplo: https://www.youtube.com/robots.txt

2. Identifique-se como um crawler.
- É uma boa prática se identificar como um crawler, definindo o nome do seu bot e um e-mail de contato. Isso pode ser feito no cabeçalho da requisição HTTP.
- Exemplo: headers = {'User-Agent': 'Nome do Bot (exemple.com)' }

3. Não faça muitas requisições em um curto período de tempo.
- Fazer muitas requisições em um curto período de tempo pode sobrecarregar o servidor e causar problemas. É uma boa prática fazer um intervalo entre as requisições.
- Exemplo: time.sleep(600)

Exemplo de como verificar se uma URL está desautorizada pelo robots.txt:
url = 'https://youtube.com/comment'  # Uma URL desautorizada

# Lista de caminhos desautorizados do robots.txt
disallowed_paths = [
    '/comment', '/feeds/videos.xml', '/get_video', # ... (todos os outros caminhos desautorizados)
]

# Verificar se a URL está desautorizada
for path in disallowed_paths:
    if path in url:
        print(f'A URL {url} está desautorizada para scraping.')
        break

# --------------------------------------------------------------------------------

Próximas etapas:

Usar o Requests para enviar requisições HTTP e receber as respostas.
Usar o Beautiful Soup para analisar o HTML e extrair as informações desejadas.
Estruturar os dados extraídos e armazená-los em um arquivo ou banco de dados.
Em páginas que requerem interação com JavaScript, usar o Selenium para interagir com a página e extrair as informações desejadas.

Por que usar inicialmente o Requests e o Beautiful Soup?:

Beautiful Soup é uma biblioteca para analisar HTML e XML, enquanto Scrapy é um framework de web scraping mais robusto que inclui muitas características prontas para uso, como middleware, pipeline para processamento de dados, e suporte para exportar dados em diferentes formatos.
Beautiful Soup é mais simples e adequado para tarefas de scraping menores e mais diretas, enquanto Scrapy é mais adequado para projetos de scraping maiores e mais complexos.

Quando usar um ou outro:

Se o seu projeto é simples e só precisa extrair dados de algumas páginas, Beautiful Soup pode ser a escolha mais fácil e rápida. Se você está planejando um projeto maior, com muitas páginas para scrape, ou precisa de funcionalidades como lidar com cookies, sessões, ou exportar dados em diferentes formatos, Scrapy seria a escolha mais apropriada.

"""

# Usando BeautifulSoup na prática:
from bs4 import BeautifulSoup

# Criando um objeto BeautifulSoup
html = "<html><body><h1>Título</h1><p>Parágrafo</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

# Acessando tags
print(soup.h1)  # Output: <h1>Título</h1>
print(soup.p)  # Output: <p>Parágrafo</p>

# Acessando o texto dentro das tags
print(soup.h1.text)  # Output: Título
print(soup.p.text)  # Output: Parágrafo

# Procurando a primeira ocorrência de uma tag
first_paragraph = soup.find("p")
print(first_paragraph.text)  # Output: Parágrafo

# Procurando todas as ocorrências de uma tag
all_paragraphs = soup.find_all("p")
for paragraph in all_paragraphs:
    print(paragraph.text)

# Procurando tags com atributos específicos
special_paragraph = soup.find("p", {"class": "especial"})
print(special_paragraph)

# Acessando tags pai e filhos
parent_tag = soup.p.parent
print(parent_tag)  # Output: <body><h1>Título</h1><p>Parágrafo</p></body>

child_tag = soup.body.h1
print(child_tag)  # Output: <h1>Título</h1>

# Acessando irmãos na árvore
next_sibling = soup.h1.find_next_sibling()
print(next_sibling)  # Output: <p>Parágrafo</p>

# Modificando o texto de uma tag
soup.h1.string = "Novo Título"
print(soup.h1)  # Output: <h1>Novo Título</h1>

# Modificando atributos de uma tag
soup.p["class"] = "novo"
print(soup.p)  # Output: <p class="novo">Parágrafo</p>

# Acessando tags com CSS selectors
soup.select("p")  # Seleciona todas as tags <p>
soup.select(".especial")  # Seleciona todas as tags com a classe 'especial'
soup.select("#id")  # Seleciona a tag com o id 'id'
soup.select("p.especial")  # Seleciona todas as tags <p> com a classe 'especial'
soup.select("p#id")  # Seleciona a tag <p> com o id 'id'
soup.select("p a")  # Seleciona todas as tags <a> dentro de uma tag <p>
soup.select("p > a")  # Seleciona todas as tags <a> que são filhas de uma tag <p>
soup.select("p + a")  # Seleciona toda a tag <a> que é irmã de uma tag <p>
soup.select("p ~ a")  # Seleciona todas as tags <a> que são irmãs de uma tag <p>
soup.select("p, a")  # Seleciona todas as tags <p> e <a>

# Extras:

# Acessando atributos de uma tag diretamente
soup.p["class"] = "novo"
soup.p["id"] = "id"
soup.p["data-attr"] = "valor"
soup.a["href"] = "https://www.example.com"
soup.a["target"] = "_blank"

print(soup.p["class"])  # Output: novo
print(soup.p["id"])  # Output: id
print(soup.p["data-attr"])  # Output: valor
print(soup.a["href"])  # Output: https://www.example.com
print(soup.a["target"])  # Output: _blank

# --------------------------------------------------------------------------------

# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from datetime import datetime


# Versão 1: Básica - Web scraping e armazenando os dados em um arquivo .txt
def scrape_and_save_to_txt():
    # Enviando uma requisição GET para a URL
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    response = requests.get("https://www.imdb.com/chart/moviemeter/", headers=header)

    # Verificando se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Analisando o HTML com Beautiful Soup
        soup = BeautifulSoup(
            response.text, "html.parser"
        )  # Também pode ser usado lxml ou html5lib

        # Localizando os títulos dos filmes na tabela
        movie_titles = [
            title.text for title in soup.find_all("h3", class_="ipc-title__text")
        ]

        # Salvando os títulos dos filmes em um arquivo .txt
        with open("movies.txt", "w") as file:
            for title in movie_titles:
                file.write(f"{title}\n")
    else:
        print("Falha ao recuperar a página. Código de status:", response.status_code)


# Versão 2: Melhor Tratamento de Dados - Salvando os dados em uma tabela Excel
def scrape_and_save_to_excel():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    response = requests.get("https://www.imdb.com/chart/moviemeter/", headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        movie_elements = soup.find_all("div", class_="cli-children")

        # Inicializando listas vazias para armazenar os dados extraídos
        movie_titles = []
        movie_links = []
        movie_years = []
        movie_durations = []
        movie_ratings = []

        for elem in movie_elements:
            # Inicializando variáveis com valores padrão para este filme
            title = link = year = duration = rating = "N/A"

            # Extraindo o título e o link do filme
            title_div = elem.find("div", class_="ipc-title-link-no-icon")
            if title_div:
                a_tag = title_div.find("a")
                if a_tag:
                    title = a_tag.h3.text
                    link = f"https://www.imdb.com{a_tag['href']}"

            # Extraindo o ano e a duração do filme
            details_div = elem.find_all("div")[2]  # Terceira div
            if details_div:
                spans = details_div.find_all("span")
                if len(spans) >= 2 and spans[1].text:
                    year = spans[0].text
                    duration = spans[1].text
                elif len(spans) == 1 and spans[0].text:
                    year = spans[0].text

            # Extraindo a avaliação do filme
            rating_span = elem.find("div", class_="cli-ratings-container")
            if rating_span:
                rating_value_span = rating_span.find_next("span")
                if rating_value_span.text:
                    rating = rating_value_span.text

            # Adicionando os valores extraídos às listas
            movie_titles.append(title)
            movie_links.append(link)
            movie_years.append(year)
            movie_durations.append(duration)
            movie_ratings.append(rating)

        # Criando um DataFrame com os dados coletados
        data = {
            "Title": movie_titles,
            "Link": movie_links,
            "Year": movie_years,
            "Duration": movie_durations,
            "Rating": movie_ratings,
        }
        df = pd.DataFrame(data)

        # Salvando o DataFrame em um arquivo Excel
        df.to_excel("movies.xlsx", index=False)
    else:
        print("Falha ao recuperar a página. Código de status:", response.status_code)


# Versão 3: Automatizada - Verificando mudanças no site a cada 10 minutos e salvando cada versão em um arquivo diferente
def automated_scrape():
    while True:
        # Chamando a função scrape_and_save_to_excel
        scrape_and_save_to_excel()

        # Criando um timestamp para o nome do arquivo
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Renomeando o arquivo com o timestamp para evitar sobrescrever arquivos antigos
        os.rename("movies.xlsx", f"movies_{timestamp}.xlsx")

        # Aguardando 10 minutos antes da próxima iteração
        t = 600
        time.sleep(t)
        print(f"Próxima iteração em {t} segundos...")


# --------------------------------------------------------------------------------

"""
Scrapy: Uma Introdução

Scrapy é uma framework de web scraping open source e colaborativa criada em 2008,
destinada a ajudar desenvolvedores a escrever, manter e implementar crawlers de web scraping de maneira eficiente.
Ela fornece todas as ferramentas necessárias para extrair dados de websites, processá-los e armazená-los no formato desejado.

Para instalar o Scrapy, use o seguinte comando:
```bash
pip install scrapy
```
# Para criar um novo projeto Scrapy, use o comando:
```bash
scrapy startproject nome_do_projeto
```

"""

"""
Fundamentos do Scrapy:
1. Spiders:
Spiders são classes onde você define como um site (ou um grupo de sites) será raspado,
incluindo como realizar a navegação, a solicitação, e o parsing dos dados.
"""

import scrapy


class ExampleSpider(scrapy.Spider):
    # O nome do spider, deve ser único dentro do projeto
    name = "example"

    # Domínios permitidos para o spider
    allowed_domains = ["example.com"]

    # Lista de URLs onde o spider começará
    start_urls = ["http://example.com"]

    # Método para parsing do conteúdo da página
    def parse(self, response):
        pass

    # logic para parsing


"""
2. Selectors:
Scrapy vem com um mecanismo de seleção poderoso para extrair dados, baseado em XPath e CSS expressions.
XPath é uma linguagem de consulta para selecionar nós de um documento XML.
CSS é uma linguagem de estilo que define seletores que associam os estilos aos elementos HTML.
"""


# Exemplo de uso de selector para obter o texto do título
def parse(self, response):
    # Usando seletores CSS
    title = response.css("title::text").get()
    titles = response.css("title::text").getall()  # Or response.css("title::text")
    link = response.css(".shout time::attr(href)").get()

    # Usando seletores XPath
    title = response.xpath("//title/text()").get()
    titles = response.xpath(
        "//title/text()"
    ).getall()  # Or response.xpath("//title/text()")
    link = response.xpath("//time/@href")

    # Usando seletores CSS e XPath
    title = response.css(".shout").xpath("./time/@datetime").getall()

    # Também é possível usar expressões regulares
    title = response.css("title::text").re(r"(\w+) World")
    titles = response.css("title::text").re(r"(\w+) World")

    # Retornando os dados extraídos
    yield {
        "title": title,
        "titles": titles,
        "link": link,
    }

    # Retornando a requisição para a próxima página
    next_page = response.css(".next a::attr(href)").get()
    if next_page:
        yield response.follow("http://example.com" + next_page, callback=self.parse)
        # Or yield response.Request("http://example.com" + next_page, callback=self.parse)

    # Retornando os dados em um item
    item = ExampleItem()
    item["title"] = title
    item["link"] = link
    yield item


"""
3. Items:
Items são contêineres simples que você usará para coletar os dados do scraping.
Eles são semelhantes aos dicionários do Python, mas com funcionalidades adicionais.
"""


def serialize_title(title):
    return title.capitalize()


class ExampleItem(scrapy.Item):
    # Definição dos campos para o item
    title = scrapy.Field(serializer=serialize_title)
    link = scrapy.Field()


"""
4. Item Pipelines:
Pipelines são processos através dos quais os items raspados são processados.
Eles são definidos como classes e são chamados sequencialmente para cada item raspado.
"""


from itemadapter import ItemAdapter


class CapitalizeTitlePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)  # Crie uma instância de ItemAdapter
        title = adapter.get("title")  # Use o método get para acessar o campo 'title'
        if title:
            adapter["title"] = title.upper()  # Modifique o item através do adapter
        return item  # Não se esqueça de retornar o item no final


# No seu settings.py, ative o pipeline:
# ITEM_PIPELINES = {'yourproject.pipelines.CapitalizeTitlePipeline': 300}

"""
5. Middlewares:
Middlewares são plug-ins customizáveis onde você pode definir comportamentos customizados para tratar das requisições e respostas.
Você pode modificar as requisições antes de serem enviadas e as respostas antes de serem processadas pelos spiders.
"""


class ExampleMiddleware:
    def process_request(self, request, spider):
        # Este método é chamado para cada requisição que o spider faz
        # Você pode modificar a requisição aqui, por exemplo, mudar o User-Agent
        request.headers["User-Agent"] = "Mozilla/5.0"
        return None  # Retorne None para continuar com o processamento da requisição


"""
6. Settings:
Você pode definir configurações para controlar o comportamento do seu projeto Scrapy.
Coloque as configurações em um arquivo chamado settings.py no diretório do seu projeto.
"""

# Exemplo de configuração em settings.py
# BOT_NAME = 'example'
# ROBOTSTXT_OBEY = False


"""
7. Scrapy Shell:
Um shell interativo para testar o código de scraping.
Use o comando:
```bash
scrapy shell 'http://example.com'
```
para iniciar o Scrapy Shell com a URL especificada.

8. Scrapy Crawl:
Comando para iniciar um spider com o nome 'example'.
```bash
scrapy crawl example
scrapy crawl example -o example.json
scrapy crawl example -o example.csv
scrapy crawl example -O example.json # Sobrescreve o arquivo se ele já existir
scrapy crawl example -O example.csv # Sobrescreve o arquivo se ele já existir
```

"""

# Ferramentas Complementares
# - ScrapyRT: Para criar APIs de web scraping.
# - Scrapy Splash: Para lidar com páginas JavaScript.
# - ScrapyD: Para deploy e agendamento de spiders.
