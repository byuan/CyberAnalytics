from pytrends.request import TrendReq
import pandas as pd

class GoogleTrends():
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def get_interest_overtime(self):
        kw_list = ["ransomware","exploit"]
        self.pytrends.build_payload(
            kw_list=kw_list,
            timeframe='today 3-m'
        )
        res = self.pytrends.interest_over_time()
        res.index = pd.to_datetime(res.index).astype(str)

        #
        # Formatting source: https://stackoverflow.com/questions/52671422/make-dictionary-with-specific-format-from-pandas-dataframe
        #

        keyword_data = {}
        for kw in kw_list:
            keyword_data[kw] = res[[kw]].agg(list)\
                .reset_index()\
                .set_axis(['t','y'], axis=1, inplace=False)\
                .to_dict('records')
        print(keyword_data)

if __name__=='__main__':
    gt = GoogleTrends()
    gt.get_interest_overtime()
