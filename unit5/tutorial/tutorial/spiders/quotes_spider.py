import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'tags': quote.css('div.tags a.tag::text').getall(),
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
