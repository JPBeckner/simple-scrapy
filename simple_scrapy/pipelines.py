# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from simple_scrapy.items import BookItem, QuoteItem


class SimpleScrapyPipeline:
    def process_item(self, item, spider):
        return self.process_book(item, spider) if isinstance(item, BookItem) else self.process_quote(item, spider)

    def process_book(self, item, spider):
        if not all(key in item._values for key in ['title', 'price']):
            raise DropItem

        item.setdefault('title', '')
        item.setdefault('price', 0.0)
        item.setdefault('in_stock', False)
        item.setdefault('rating', 0)
        item.setdefault('image_url', '')

        spider.logger.info(f"Book found - Title: {item['title']} | Stock: {item['in_stock']}")

        return item

    def process_quote(self, item, spider):
        if not all(key in item._values for key in ['quote', 'author']):
            raise DropItem

        item.setdefault('quote', '')
        item.setdefault('author', '')
        item.setdefault('tags', '')

        spider.logger.info(f"Quote found - Author: {item['author']}")

        return item
