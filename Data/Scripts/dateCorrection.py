import pandas as pd
import datetime as dt

data = pd.read_csv("/home/bhavya16/Desktop/FlairifyMe/Data/CSV/preprocessedData.csv")
data_withStemming = pd.read_csv("/home/bhavya16/Desktop/FlairifyMe/Data/CSV/preprocessedData_withStemming.csv")

def get_date(created):
	return dt.datetime.fromtimestamp(created)


data["timestamp"] = data["date"].apply(get_date)
data_withStemming["timestamp"] = data_withStemming["date"].apply(get_date)

data.to_csv("./testing.csv")
data_withStemming.to_csv("./testing_withStemming.csv")