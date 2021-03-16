# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BookPipeline:
    def process_item(self, item, spider):
        if not all(key in item._values for key in ['title', 'price']):
            raise DropItem

        item.setdefault('title', '')
        item.setdefault('price', 0.0)
        item.setdefault('in_stock', False)
        item.setdefault('rating', 0)
        item.setdefault('image_url', '')

        spider.logger.info(f"Book found - Title: {item['title']} | Stock: {item['in_stock']}")

        return item
