# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from .books import BooksSpider
from .quotes import QuotesSpider

__all__ = ['BooksSpider', 'QuotesSpider']
