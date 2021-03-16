from scrapy.crawler import CrawlerProcess

from simple_scrapy.spiders import BooksSpider


def run():
    crawler = CrawlerProcess()
    crawler.crawl(BooksSpider)
    crawler.start()

if __name__ == "__main__":
    run()
