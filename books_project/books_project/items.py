# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksprojectItem(scrapy.Item):
    title = scrapy.Field()  # Título do livro
    price_uk_pounds = scrapy.Field()  # Preço final do livro em GBP
    price_us_dollar = scrapy.Field()  # Preço final do livro em USD
    price_br_real = scrapy.Field()  # Preço final do livro em BRL
    rating = scrapy.Field()  # Avaliação do livro
    availability = scrapy.Field()  # Disponibilidade do livro
    url = scrapy.Field()  # URL da página de detalhes do livro
    stock = scrapy.Field()  # Quantidade de estoque do livro
    genre = scrapy.Field()  # Gênero do livro
    reviews = scrapy.Field()  # Número de reviews do livro
