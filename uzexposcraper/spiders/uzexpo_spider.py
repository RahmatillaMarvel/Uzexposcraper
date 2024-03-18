import scrapy
from datetime import date
from uzexposcraper.items import NewsItem

class UzexpoSpiderSpider(scrapy.Spider):

    writing_system = {
        'lat': 'uz/',
        'krill': 'oz',
        'eng': 'en/',
        'rus': 'ru/'

    }
    name = "uzexpo_spider"
    # allowed_domains = ["www.uzexpocentre.uz"]
    def __init__(self, /, *, ws='lat', **kwargs)-> None:

        self.ws: str = ws
        self.start_urls: list[str] = [f'https://www.uzexpocentre.uz/{self.writing_system[self.ws]}/news']
        super().__init__(**kwargs)

    custom_settings: dict[str, dict[str, str]] = {
        'FEEDS': {
            'web/%(name)s/%(ws)s/uzexpo.json': {'format': 'json', 'encoding': 'utf8', 'fields': ['url', 'title', 'text', 'creation_date', 'access_date'], 'overwrite': True},
        }
    }


    def parse(self, response):

        news_list = response.css('.all-news1 .row div')
        next_page: str = response.xpath('//div[contains(@class, "pagination")]/ul/li/a[@rel="next"]/@href').get()
        for news in news_list:
            url: str = news.css('a::attr(href)').get()
            if not url is None:
                yield response.follow(url, self.parse_news)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_news(self, response):
        news_items = NewsItem()
        news_items['url'] = response.url
        news_items['title'] = response.css('.news-content__header h2::text').get()
        news_items['text'] = response.css('.content p::text').getall()
        news_items['creation_date'] = response.css('.date::text').get()
        news_items['access_date'] = date.today()
        yield news_items
        

