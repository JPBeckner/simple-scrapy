from re import findall
from typing import List

from scrapy import Spider, Request, Selector
from scrapy.http import Response

from simple_scrapy.items import QuoteItem


class QuotesSpider(Spider):
    name = 'quotes'
    base_url = 'http://quotes.toscrape.com'
    start_urls = [base_url]

    custom_settings = {
        'FEEDS': {  
            'saved-data-extracted/quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            }
        }
    }

    def parse(self, response: Response):
        next_page = response.xpath("//*[contains(@class, 'next')]/a/@href").get('')
        if next_page:
            yield Request(
                url=f"{self.base_url}{next_page}",
                callback=self.parse
            )
        
        quote: Selector
        for quote in response.xpath("//*[contains(@class, 'quote')]"):
            quote_text: str = quote.xpath("./span[contains(@class, 'text')]/text()").get('')
            author: str = quote.xpath("./span/small[contains(@class, 'author')]/text()").get('')
            tag: Selector
            tags: List[str] = [
                    tag.xpath("./text()").get('').strip().lower() 
                    for tag in quote.xpath("./div[contains(@class, 'tags')]/a")
                ]
            
            yield QuoteItem({
                'quote': quote_text,
                'author': author,
                'tags': tags
            })
