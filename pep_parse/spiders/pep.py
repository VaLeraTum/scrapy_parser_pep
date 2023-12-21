import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep = response.css('tbody tr a[href^="pep-"]')
        for link in pep:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep = response.css('.page-title::text').get().split()
        yield {
            'number': pep[1],
            'name': ' '.join(pep[3:]),
            'status': response.css('abbr::text').get()
        }
