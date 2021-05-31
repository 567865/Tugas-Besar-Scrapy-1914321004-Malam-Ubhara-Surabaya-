import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/super-detective-in-the-fictional-world/',
	    'https://www.worldnovel.online/novel/a-record-of-a-mortals-journey-to-immortality/',
	    'https://www.worldnovel.online/novel/gourmet-of-another-world/',
	    'https://www.worldnovel.online/novel/versatile-mage/',
	    'https://www.worldnovel.online/novel/i-have-countless-legendary-swords/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')