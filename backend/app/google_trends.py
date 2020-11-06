from pytrends.request import TrendReq
import pandas as pd
from itertools import zip_longest
from app.db_utility import DBUtility

class GoogleTrends():
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
        self.db = DBUtility()
    
    def _grouper(self, iterable, size):
        return (iterable[pos:pos + size] for pos in range(0, len(iterable), size))
    
    def get_interest_overtime(self):
        words_dict = self.db.query('select word from keywords')
        keywords_list = [row['word'] for row in words_dict]
        print(keywords_list)

        keyword_data = {}
        for kw_list in self._grouper(keywords_list, 5):
            self.pytrends.build_payload(
                kw_list=kw_list,
                timeframe='today 3-m'
            )
            res = self.pytrends.interest_over_time()
            res.index = pd.to_datetime(res.index).astype(str)

            for kw in kw_list:
                # Formatting source: https://stackoverflow.com/questions/52671422/make-dictionary-with-specific-format-from-pandas-dataframe
                keyword_data[kw] = res[[kw]].agg(list)\
                    .reset_index()\
                    .set_axis(['x','y'], axis=1, inplace=False)\
                    .to_dict('records')
        return keyword_data

if __name__=='__main__':
    gt = GoogleTrends()
    gt.get_interest_overtime()
