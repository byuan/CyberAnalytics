
import scrapy

class DataCollectionSpider(scrapy.Spider):
    name="threats"

    def start_requests(self):
        urls=["https://threatpost.com/category/vulnerabilities"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        x=17
        artNum=0
        for x in range (17, 55):
            link=response.css("a::attr(href)")[x].get()
#            if("author" in link):
#                pass
#            else: 
            yield scrapy.Request(link, callback=self.parse2)
#            text=response.xpath('//body//p//text()').extract()
#            filename="article_" + str(artNum) + ".txt"
#            with open(filename, "ab") as f:
#                for items in text:
#                     f.write(items.encode('utf-8'))
#            f.close()
#            artNum=artNum+1
            x=x+2

    def parse2(self, response):
#        artNum=0
        text=response.xpath('//body//p//text()').extract()
        filename="articles.txt"
        with open(filename, "ab") as f:
            for items in text:
                f.write(items.encode('utf-8'))
            f.write("\n")
            f.write("\n")
        f.close()
#        artNum=artNum+1
