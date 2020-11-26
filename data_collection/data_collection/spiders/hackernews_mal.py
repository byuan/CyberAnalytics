import scrapy #Python Package Used for Data Collection
import mysql.connector #Python Package Used for MYSQL Database Connecting
from datetime import datetime

class DataCollectionSpider(scrapy.Spider):
    name="hackernews_mal"
    start_urls=["https://thehackernews.com/search/label/Malware/"]

    def parse(self, response):
        temp=[]
        links=[]
        a_tags=response.xpath("//a")

        for tags in a_tags:
            link=tags.xpath("@href").extract_first()
            temp.append(link)

        for link in temp:
            if("https://thehackernews.com/2020" in link):
                yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        db=mysql.connector.connect(
            host="192.168.205.5",
            user="admin",
            password="c00Lm@rJ3to",
            database="global_threat_thermometer"
        )
        dbcontroller=db.cursor()

        title=response.css('title::text').get()

        url=response.url

        date=response.xpath('//div[@class="postmeta"]/span/text()').extract()
        date=' '.join(date)
        dt=datetime.strptime(date, '%B %d, %Y')

        text=response.xpath('//div[@id="articlebody"]/p/text()').extract()
        txt=' '.join(text)

        wcount=len(txt.split())

        ###################### START-COMPARE ###########################
        dupes=[]
        dbcontroller.execute("SELECT title FROM raw_articles;")
        result=dbcontroller.fetchall()
        db.commit()

        for z in result:
            dupes.append(z[0])

        if title not in dupes:
            sql="INSERT INTO raw_articles (title, URL, date, article, fk_sources_id, total_word_count) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(title, url, dt, txt, 2, wcount)
            dbcontroller.execute(sql, val)
            db.commit()
            print(title)
            print("DID SUBMIT TO DATABASE")
        else:
            print(title)
            print("DID NOT SUBMIT TO DATABASE")

        ###################### START-COMPARE ###########################
