# simple-scrapy
Simple Scrapy project example

### Spiders

#### Books
Spider that scrape the site [books to scrape](http://books.toscrape.com/index.html)
  * data returned: 
  ```json
    {
        "title": "type: string",
        "price": "type: float",
        "in_stock": "type: bool",
        "rating": "type: int",
        "image_url": "type: string",
    }
  ```

#### Quotes
Spider that scrape the site [quotes to scrape](http://quotes.toscrape.com)
  * data returned: 
  ```json
    {
        "author": "type: string",
        "quote": "type: string",
        "tags": "type: list(string,)",
    }
  ```

