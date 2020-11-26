import scrapy #Python Package Used for Data Collection
import mysql.connector #Python Package Used for MYSQL Database Connecting
from datetime import datetime #Python Package Used for Date/Time Conversion (For Database)

class DataCollectionSpider(scrapy.Spider):
    name="threatpost_mal"
    start_urls=["https://threatpost.com/category/malware-2/"]

    def parse(self, response):
        temp=[]
        links=[]
        a_tags=response.xpath("//a")

        #Extract All Links on Main Page
        for tags in a_tags:
            link=tags.xpath("@href").extract_first()
            temp.append(link)

        #For Parsing Out Bad Links (Depends on Website)
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
        no_dupes.pop(0) #Pop First URL because URL=Main URL

        #Send Links to 2nd Function, Traverse Each Link
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

        #Grab Article Title
        ti=response.css('title::text').get()
        title=ti.split(' | ')
        title=title[0]

        #Grab Article URL
        url=response.url

        #Grab Article Date
        date=response.css('time::attr(datetime)').get()
        date=date.encode('UTF-8')
        date=date.split('T')
        dt=datetime.strptime(date[0], '%Y-%m-%d')

        #Grab Article Body Text
        text=response.xpath('//div[@class="c-article__content js-reading-content"]/p/text()').extract()
        txt=' '.join(text)

        wcount=len(txt.split())

        ###################### START-COMPARE ###########################
        dupes=[]
        dbcontroller.execute("SELECT title FROM raw_articles;") #Query Entries Currently Present
        result=dbcontroller.fetchall()
        db.commit()

        #Store Titles in Database in List for Comparison
        for z in result:
            dupes.append(z[0])

        if title not in dupes:
            sql="INSERT INTO raw_articles (title, URL, date, article, fk_sources_id, total_word_count) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(title, url, dt, txt, 1, wcount)
            dbcontroller.execute(sql, val)
            db.commit()
            print(title) #For Debugging Purposes
            print("DID SUBMIT TO DATABASE") #For Debugging Purposes
        else:
            print(title) #For Debugging Purposes
            print("DID NOT SUBMIT TO DATABASE") #For Debugging Purposes

        ###################### START-COMPARE ###########################
