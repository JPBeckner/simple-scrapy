# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class BookItem(Item):

    title = Field()
    price = Field()
    in_stock = Field()
    rating = Field()
    image_url = Field()
