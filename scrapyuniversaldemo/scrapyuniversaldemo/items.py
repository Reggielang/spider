# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    cover = scrapy.Field()
    categories = scrapy.Field()
    published_at = scrapy.Field()
    drama = scrapy.Field()
    score = scrapy.Field()

