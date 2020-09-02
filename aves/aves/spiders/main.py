import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "main"

    def start_requests(self):
        urls = [
            'https://www.wikiaves.com/109',
            'https://www.wikiaves.com/1093',
            'https://www.wikiaves.com/10923',
            'https://www.wikiaves.com/1091',
            'https://www.wikiaves.com/1145'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        autor = re.findall(r"data='(.*)'>", str(response.xpath('//label[contains(.,"Autor")]/following-sibling::a/text()')))
        yield{
            'Autor': autor
        }