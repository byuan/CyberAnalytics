from datetime import datetime
from datetime import timedelta
from app.global_threats import GlobalThreats
from app.db_utility import DBUtility


class Thermometer():
    def __init__(self):
        self.db = DBUtility()

    def get_historical(self):
        return self.db.query("select score as 'y',\
                DATE_FORMAT(date, '%%Y-%%m-%%d') as 'x'\
                from thermometer\
                order by date asc")

if __name__=='__main__':
    start_date = "2020-10-01"

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.today()

    gt = GlobalThreats()
    db = DBUtility()

    print(gt.get_minimum_score_as_of(start))
    print

    while start < end:
        print(start)
        min_score = gt.get_minimum_score_as_of(start)[0]['weighted count']
        max_score = gt.get_maximum_score_as_of(start)[0]['weighted count']
        todays_score = gt.get_todays_score_as_of(start)
        if todays_score:
            todays_score = todays_score[0]['weighted count']
            print(min_score, max_score, todays_score)
            todays_thermometer = int(round(((todays_score - min_score) * 100) / (max_score - min_score)))
            print(todays_thermometer)
            query = "insert into thermometer (score, date) values (%s,'%s')" % (todays_thermometer, start.strftime('%Y-%m-%d'))
            db.query(query, statement='insert')

        start = start + timedelta(days=1)