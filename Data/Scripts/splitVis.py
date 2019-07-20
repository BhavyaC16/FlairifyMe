import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/bhavya16/Desktop/FlairifyMe/Data/CSV/preprocessedData.csv")
flair = ['AMA','Business Finance Policy','Food','Sports','Politics','Science Technology','Policy Economy','Photography','Scheduled','Reddiquette','Non-Political','AskIndia','Entertainment']
plt.figure()
df.flair.value_counts().plot(kind='bar');
plt.show()