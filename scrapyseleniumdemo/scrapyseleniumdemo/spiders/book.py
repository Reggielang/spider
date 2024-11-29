import re
from typing import Iterable

import scrapy
from scrapy import Request

from scrapyseleniumdemo.items import BookItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["spa5.scrape.center"]
    start_urls = ["https://spa5.scrape.center"]
    base_url = "https://spa5.scrape.center"

    def start_requests(self) -> Iterable[Request]:
        start_url = f'{self.base_url}/page/1'
        yield Request(url=start_url, callback=self.parse_index)
    def parse_index(self, response):
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            yield Request(url=detail_url, callback=self.parse_detail,priority=2)

        match = re.search(r'page/(\d+)', response.url)
        if not match:return
        page = int(match.group(1))+1
        next_url = f'{self.base_url}/page/{page}'
        yield Request(url=next_url, callback=self.parse_index)


    def parse_detail(self, response):
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract()
        score = response.css('.score::text').extract_first()
        price = response.css('.price span::text').extract_first()
        cover = response.css('.cover::attr(src)').extract_first()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
        yield item

