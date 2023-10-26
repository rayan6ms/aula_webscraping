# flake8: noqa
import scrapy
from books_project.items import BooksprojectItem


class BooksSpider(scrapy.Spider):
    name = "books"  # Nome único do spider
    start_urls = ["https://books.toscrape.com/"]  # URLs iniciais para scraping

    # Método de parsing para processar a página inicial e cada página de produtos
    def parse(self, response):
        for book in response.css(".product_pod"):  # Itera sobre cada livro na página
            item = BooksprojectItem()  # Cria uma nova instância do item
            # Extrai e armazena os dados do livro
            item["title"] = book.css("h3 a::attr(title)").get()
            item["price_uk_pounds"] = book.css(".price_color::text").get()[1:]
            item["rating"] = book.css("p::attr(class)").re("star-rating ([A-Za-z]+)")[0]
            item["url"] = book.css("h3 a::attr(href)").get()
            # Faz uma requisição para a página de detalhes do livro
            yield response.follow(
                url=item["url"], callback=self.parse_book, meta={"item": item}
            )
            # Or yield scrapy.Request(url=response.urljoin(item["url"]), callback=self.parse_book, meta={"item": item})

        # Verifica se há uma próxima página e, se houver, faz uma requisição para ela
        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
            # Or yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    # Método de parsing para processar a página de detalhes de cada livro
    def parse_book(self, response):
        item = response.meta["item"]  # Recupera o item passado como meta
        # Extrai e armazena dados adicionais da página de detalhes
        stock_text = response.css(".instock.availability::text").re(
            "\((\d+) available\)"
        )
        item["stock"] = int(stock_text[0]) if stock_text else 0
        availability_text = " ".join(
            response.css(".product_main .availability::text").re("([A-Za-z]+)")[:-1]
        )
        item["availability"] = (
            "In stock" in availability_text if availability_text else False
        )
        item["genre"] = response.css(".breadcrumb li:nth-child(3) a::text").get()
        reviews_text = response.css("table.table tr:nth-child(7) td::text").get()
        item["reviews"] = (
            int(reviews_text) if reviews_text and reviews_text.isdigit() else 0
        )

        yield item  # Retorna o item preenchido
