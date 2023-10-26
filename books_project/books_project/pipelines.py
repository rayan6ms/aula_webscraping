# flake8: noqa

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class BooksProjectPipeline:
    def process_item(self, item, spider):
        # Convertendo a avaliação para um número
        rating_dict = {
            "Zero": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }
        item["rating"] = rating_dict.get(item["rating"], 0)

        # Convertendo o preço para float e criando campos para diferentes moedas
        price_uk_pounds = float(item["price_uk_pounds"].replace("£", ""))
        item["price_uk_pounds"] = price_uk_pounds
        item["price_us_dollar"] = float(f"{(price_uk_pounds * 1.21):.2f}")
        # Supondo uma taxa de câmbio de 1.21
        item["price_br_real"] = float(f"{(price_uk_pounds * 6.06):.2f}")
        # Supondo uma taxa de câmbio de 6.06

        return item
