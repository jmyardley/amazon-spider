import scrapy


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspider'
    allowed_domains = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7/']

    def start_requests(self):
        url = "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7/"

        headers =  {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
            }
        yield scrapy.http.Request(url, headers=headers)


    def parse(self, response):
        REVIEW = '.a-section.review.aok-relative'
        for review in response.css(REVIEW):
            obj = {
                'id': review.css('::attr(id)').extract_first(),
                'title': review.css('.a-size-base.review-title').css('span::text').get(),
                'date': review.css('.review-date::text').extract(),
                'rating': review.css('.review-rating').css('span::text').extract()
            }
            
            yield obj
