
import scrapy

class DataCollectionSpider(scrapy.Spider):
    name="mal"
    start_urls=["https://threatpost.com/category/malware-2/"]

    def parse(self, response):
        f=open("mal_links.txt", "ab")
        temp=[]
        links=[]
        a_tags=response.xpath("//a")

        for tags in a_tags:
            link=tags.xpath("@href").extract_first()
            temp.append(link)

        for link in temp:
            if("comment" in link or "author" in link):
                pass
            elif("threatpost" in link):
                for char in link:
                    if char.isdigit():
                        links.append(link)
                        break
                    else:
                        pass
            else:
                pass

        no_dupes=list(dict.fromkeys(links))
        no_dupes.pop(0)
        f.write(str(no_dupes))
        f.close()

        for link in no_dupes:
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        t=open("mal_titles.txt", "ab")
        titles=[]
        b=open("mal_body.txt", "ab")
        body=[]
        d=open("mal_dates.txt", "ab")
        dates=[]

        titles.append(response.css('title::text').get())
        t.write(str(titles))
        t.close()

        dates.append(response.css('time::attr(datetime)').get())
        d.write(str(dates))
        d.close()

        text=response.xpath('//div[@class="c-article__content js-reading-content"]/p/text()').extract()
        body.append(text)
        b.write(str(body))
        b.close()
