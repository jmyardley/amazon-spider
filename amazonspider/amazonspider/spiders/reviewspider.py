import scrapy


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspider'
    allowed_domains = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7']
    start_urls = ['http://https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7/']

    def parse(self, response):
        pass
