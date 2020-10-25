from db_utility import DBUtility
import json

class GlobalThreats():
    def __init__(self):
        self.db = DBUtility()
    
    def add_keyword(self, request_json):
        print(request_json)
    
    def update_keyword(self, request_json):
        print(request_json)
    
    def get_keywords(self):
        return self.db.query('select id,word,weight,enabled from keywords')
    
    def get_articles(self):
        return self.db.query("select id,title,date,\
                CAST(FLOOR(SUM(LENGTH(article) - LENGTH(REPLACE(article, ' ', '')) + 1)) as SIGNED) as word_count\
                from raw_articles group by id")
    
    def get_keywords_analysis(self):
        return self.db.query("select kw.word as 'word',CAST(SUM(kwa.count) as SIGNED) as 'count', \
                CAST(SUM(kwa.weighted_count) as SIGNED) as 'weighted count', DATE_FORMAT(ra.date, '%%Y-%%m-%%d') as 'date' \
                from keywords as kw, keywords_analysis as kwa, raw_articles as ra \
                where kw.id = kwa.fk_keyword_id \
                and ra.id = kwa.fk_raw_article_id \
                group by kw.word, ra.date \
                order by ra.date asc;")

