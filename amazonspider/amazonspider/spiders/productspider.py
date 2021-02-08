import scrapy


class ProductspiderSpider(scrapy.Spider):
    name = 'productspider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7/']

    def start_requests(self):
        url = "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7/"

        headers =  {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
            }
        yield scrapy.http.Request(url, headers=headers)


    def parse(self, response):
        pass
