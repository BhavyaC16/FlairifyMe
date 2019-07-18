import pandas as pd
import numpy as np

df1 = pd.read_csv('./preprocessedData.csv')
df1['split'] = np.random.randn(df1.shape[0], 1)

a = np.random.rand(len(df1)) <= 0.75

train1 = df1[a]
test1 = df1[~a]
train1.to_csv('./train.csv')
test1.to_csv('./test.csv')

df2 = pd.read_csv('./preprocessedData_withStemming.csv')
df2['split'] = np.random.randn(df2.shape[0], 1)

b = np.random.rand(len(df2)) <= 0.75

train2 = df1[b]
test2 = df1[~b]
train2.to_csv('./train_withStemming.csv')
test2.to_csv('./test_withStemming.csv')