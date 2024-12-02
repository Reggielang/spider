import scrapy


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["sp5.scrape.center"]
    start_urls = ["https://sp5.scrape.center"]
    http_user = "admin"
    http_pass = "admin"

    def parse(self, response):
        pass
