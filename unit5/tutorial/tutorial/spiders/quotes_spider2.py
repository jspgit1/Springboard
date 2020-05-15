import scrapy


class QuotesSpider(scrapy.Spider):
    name = "xpath-scraper"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class=\'quote\']'):
            yield {
                'tags': quote.xpath('//div[@class=\'tags\']/a/text()').getall(),
                'text': quote.xpath('//span[@class=\'text\']/text()').get(),
                'author': quote.xpath('//span/small/text()').get(),
            }
