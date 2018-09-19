from pytrends.request import TrendReq

pytrends = TrendReq()

interest_df = pytrends.get_historical_interest(["学生フォーミュラ"], year_start=2008)
print(interest_df)