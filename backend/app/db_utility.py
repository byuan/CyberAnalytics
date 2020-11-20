import pymysql
import app.settings as settings

class DBUtility():
    def __init__(self):
        self.db = pymysql.connect(host=settings.DB_HOST,
                                user=settings.DB_USER,
                                password=settings.DB_PASSWORD,
                                db=settings.DB_DATABASE,
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)
    
    def query(self, query, params=(), statement='select'):
        try:
            if statement == 'select':
                with self.db.cursor() as cursor:
                    cursor.execute(query % params)
                    return cursor.fetchall()
            else:
                with self.db.cursor() as cursor:
                    cursor.execute(query % params)
                    self.db.commit()
        except Exception as e:
            print(e, flush=True)
            raise(e)
        
if __name__=='__main__':
    db = DBUtility()
    print(db.query('select %s, %s, %s from keywords', params=('word','weight','enabled')))