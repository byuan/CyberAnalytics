import scrapy

class DataCollectionSpider(scrapy.Spider):
    name="threats"

    def start_requests(self):
        urls=["https://threatpost.com/category/vulnerabilities"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page=response.url.split("/")[-2]
        article1=response.css("a::attribute(href)")[17].get()
        filename="vulns.html"
        with open(filename, "wb") as f:
            f.write(article1)
        self.log("Saved file %s" % filename)
