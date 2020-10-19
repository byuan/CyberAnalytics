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

