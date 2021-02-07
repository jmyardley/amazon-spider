import scrapy


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def start_requests(self):
        url = "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1"

        headers =  {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
            }
        yield scrapy.http.Request(url, headers=headers)


    def parse(self, response):
        REVIEW = '.a-section.review.aok-relative'
        for review in response.css(REVIEW):
            obj = {
                'id': review.css('::attr(id)').extract_first(),
                'title': review.css('.review-title').css('span::text').get(),
                'date': review.css('.review-date::text').extract(),
                'rating': review.css('.review-rating').css('span::text').extract(),
                'text': review.css('.review-text-content').css('span::text')[1].extract()
            }
            
            yield obj

        nextpageel = response.css('.a-last').css('a::attr(href)').get()
        if nextpageel:
            yield scrapy.Request(
                response.urljoin(nextpageel),
                callback=self.parse
            )
