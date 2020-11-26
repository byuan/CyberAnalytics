import scrapy #Python Package Used for Data Collection
import mysql.connector #Python Package Used for MYSQL Database Connecting
from datetime import datetime

class DataCollectionSpider(scrapy.Spider):
    name="threatpost_vuln"
    start_urls=["https://threatpost.com/category/vulnerabilities/"]

    def parse(self, response):
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
        no_dupes.pop(1)

        print(no_dupes)

        for link in no_dupes:
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        db=mysql.connector.connect(
            host="192.168.205.5",
            user="admin",
            password="c00Lm@rJ3to",
            database="global_threat_thermometer"
        )
        dbcontroller=db.cursor()

        ti=response.css('title::text').get()
        title=ti.split(' | ')
        title=title[0]

        url=response.url

        date=response.css('time::attr(datetime)').get()
        date=date.encode('UTF-8')
        date=date.split('T')
        dt=datetime.strptime(date[0], '%Y-%m-%d')

        text=response.xpath('//div[@class="c-article__content js-reading-content"]/p/text()').extract()
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
            val=(title, url, dt, txt, 1, wcount)
            dbcontroller.execute(sql, val)
            db.commit()
            print(title)
            print("DID SUBMIT TO DATABASE")
        else:
            print(title)
            print("DID NOT SUBMIT TO DATABASE")

        ###################### START-COMPARE ###########################
