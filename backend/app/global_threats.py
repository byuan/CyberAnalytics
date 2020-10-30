from app.db_utility import DBUtility
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
    
    def get_keywords_analysis(self, n_days=7):
        return self.db.query("select kw.word as 'word',\
                CAST(SUM(kwa.count) as SIGNED) as 'count',\
                CAST(SUM(kwa.weighted_count) as SIGNED) as 'weighted count',\
                DATE_FORMAT(ra.date, '%%Y-%%m-%%d') as 'date'\
                from keywords as kw, keywords_analysis as kwa, raw_articles as ra\
                inner join (\
                    select max(ra.date) as max_date from raw_articles as ra, keywords_analysis as kwa\
                    where ra.id = kwa.fk_raw_article_id\
                ) md\
                where kw.id = kwa.fk_keyword_id\
                and ra.id = kwa.fk_raw_article_id\
                and ra.date > DATE_ADD(md.max_date, interval -%s day)\
                group by kw.word, ra.date\
                order by ra.date asc", params=(n_days))
    
    def get_minimum_score(self):
        return self.db.query("select CAST(SUM(kwa.weighted_count) as SIGNED) as 'weighted count',\
                ra.date as 'date'\
                from keywords as kw, keywords_analysis as kwa, raw_articles as ra\
                where kw.id = kwa.fk_keyword_id\
                and ra.id = kwa.fk_raw_article_id\
                group by ra.date\
                order by sum(kwa.weighted_count) asc\
                limit 1")
    
    def get_maximum_score(self):
        return self.db.query("select CAST(SUM(kwa.weighted_count) as SIGNED) as 'weighted count',\
                ra.date as 'date'\
                from keywords as kw, keywords_analysis as kwa, raw_articles as ra\
                where kw.id = kwa.fk_keyword_id\
                and ra.id = kwa.fk_raw_article_id\
                group by ra.date\
                order by sum(kwa.weighted_count) desc\
                limit 1;")
    
    def get_todays_score(self):
        return self.db.query("select CAST(SUM(kwa.weighted_count) as SIGNED) as 'weighted count',\
            ra.date as 'date'\
            from keywords as kw, keywords_analysis as kwa, raw_articles as ra\
            where kw.id = kwa.fk_keyword_id\
            and ra.id = kwa.fk_raw_article_id\
            group by ra.date\
            order by ra.date desc\
            limit 1;")

