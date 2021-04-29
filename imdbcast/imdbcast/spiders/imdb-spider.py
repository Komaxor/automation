import scrapy
from ..items import ImdbcastItem


class ImdbSpider(scrapy.Spider):
    name = 'cast'
    start_urls = [
        'https://www.imdb.com/chart/top/'
    ]

    def parse(self, response):
        for url in response.css(".titleColumn a::attr(href)").extract():
            request = scrapy.Request(
                response.urljoin(url), callback=self.parseSite)
            yield request

    def parseSite(self, response):
        full_cast = response.css(".primary_photo+ td a::text").extract()
        for actor in full_cast:
            cast = ImdbcastItem()
            cast["name"] = str(actor).strip()
            yield cast
