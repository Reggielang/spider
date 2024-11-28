import json
from typing import Iterable
import scrapy
from scrapy import Request
from scrapyspidermiddlewaredemo.items import DemoItem


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_url = "https://www.httpbin.org/get"

    def start_requests(self) -> Iterable[Request]:
        for i in range(5):
            url = f'{self.start_url}?query={i}'
            yield Request(url, callback=self.parse)

    def parse(self, response):
        item = DemoItem(**response.json())
        yield item
