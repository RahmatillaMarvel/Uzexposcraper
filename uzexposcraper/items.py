# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UzexposcraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    creation_date = scrapy.Field()
    access_date = scrapy.Field()

