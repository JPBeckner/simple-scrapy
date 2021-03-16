import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com/index.html']
    start_urls = ['http://books.toscrape.com/index.html/']

    def parse(self, response):
        pass
