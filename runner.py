from scrapy.crawler import CrawlerProcess

from simple_scrapy.spiders import *


def run():
    crawler = CrawlerProcess()
    crawler.crawl(BooksSpider)
    crawler.crawl(QuotesSpider)
    crawler.start()

if __name__ == "__main__":
    run()
