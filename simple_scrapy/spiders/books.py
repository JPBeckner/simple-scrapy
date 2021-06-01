from re import findall

from scrapy import Spider, Request, Selector
from scrapy.http import Response

from simple_scrapy.items import BookItem


class BooksSpider(Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/index.html']
    base_url = start_urls[0].replace('/index.html', '')

    rating = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }

    custom_settings = {
        'FEEDS': {  
            'saved-data-extracted/books.json': {
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
        """
        Método default chamado pelo scrapy após as requests iniciais.
        """

        first_page, last_page = findall(r'\d+', response.xpath("//*[contains(@class, 'pager')]/*/text()").get('0 0'))
        for page in range(int(first_page), int(last_page)):
            yield Request(
                url=f"{self.base_url}/catalogue/page-{page}.html",
                callback=self.parse_pages
            )

    def parse_pages(self, response: Response):
        product: Selector
        for product in response.xpath("//*[contains(@class, 'product_pod')]"):
            
            title: str = product.xpath("./h3/a/@title").get('')
            
            img_src = product.xpath("./div[@class='image_container']/a/img/@src").get('').replace('..', '')
            image_url = f"{self.base_url}{img_src}"

            rating: int = self.rating.get(product.xpath("./p/@class").get(''), 0)

            product_price = product.xpath("./div[@class='product_price']")
            price = float('.'.join(findall(r'\d+', product_price.xpath("./p[contains(@class, 'price')]/text()").get(''))))
            stock: bool = 'ok' in product_price.xpath("./p[contains(@class, 'instock')]/i/@class").get('')

            yield BookItem({
                'title': title,
                'price': price,
                'in_stock': stock,
                'rating': rating,
                'image_url': image_url,
            })
