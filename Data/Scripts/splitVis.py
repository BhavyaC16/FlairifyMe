#import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/bhavya16/Desktop/FlairifyMe/Data/CSV/preprocessedData.csv")
'''
flair = ['AMA','Business Finance Policy','Food','Sports','Politics','Science Technology','Policy Economy','Photography','Scheduled','Reddiquette','Non-Political','AskIndia','Entertainment']

collect_num_comments = []
collect_num_ups = []

for i in flair:
	comments = 0
	ups = 0
	for index, row in df.iterrows():
		if(row['flair']==i):
			comments+=int(row['num_comments'])
			ups+=int(row['ups'])
	collect_num_comments.append(comments)
	collect_num_ups.append(ups)

print(collect_num_ups)
print(collect_num_comments)
'''
#plt.figure()
#df.flair.value_counts().plot(kind='bar');
#plt.savefig('DataSplit.png', bbox_inches = "tight")
#plt.show()

time = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
collect_timestamps = []
for i in time:
	count = 0
	for index,row in df.iterrows():
		if(str(row['date'])[-8:-6]==i):
			count+=1
	collect_timestamps.append(count)
print(collect_timestamps)