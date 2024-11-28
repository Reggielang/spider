from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.http import JsonRequest,FormRequest


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org"]

    start_url = 'https://www.httpbin.org/get'
    start_url2 = 'https://www.httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    cookies = {
        'name': 'germey',
        'age': '26'
    }

    data = {
        'name': 'germey',
        'age': '26'
    }
    #改写初始request
    def start_requests(self) -> Iterable[Request]:
        # for offset in range(5):
        #     url = self.start_url+f'?offset={offset}'
        #     yield Request(url, headers=self.headers, cookies=self.cookies,
        #                   callback=self.parse_response,meta={'offset':offset})
        yield FormRequest(self.start_url2, formdata=self.data,
                           callback=self.parse_response)

        yield JsonRequest(self.start_url2, data=self.data,
                           callback=self.parse_response)

    def parse_response(self, response):
        print('url',response.url)
        print('request',response.request)
        print('status',response.status)
        print('headers',response.headers)
        print('text',response.text)
        print('meta',response.meta)