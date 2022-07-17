import scrapy


class ScrapyRankSpiderSpider(scrapy.Spider):
    name = 'scrapy_rank_spider'
    allowed_domains = ['www.businessinsider.com']
    start_urls = [
        'https://www.businessinsider.com/the-100-most-popular-rock-bands-of-all-time-2018-9']

    def parse(self, response):
        # \33 -queen-98 > div > div.slide-title.clearfix > h2
        # #\31 -the-beatles-100 > div > div.slide-title.clearfix > h2
        artists = response.xpath('//div/div/div/div/h2/text()')
        for artist in artists:
            ranking, name = artist.get().split(". ")
            yield {
                'Ranking': ranking,
                'name': name
            }
