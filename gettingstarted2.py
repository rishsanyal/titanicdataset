import csv as csv
import numpy as np
import pandas as pd
'''
csv_file_object = csv.reader(open('/Users/rsanyal//Documents/Titanic/train.csv','r'))
header = next(csv_file_object)
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)
data2 = np.array(data[0:15,5])
print(data2)
'''
df = pd.read_csv('train.csv',header = 0)
print(df.head(3))
print(df.describe())
def printr(df2):
    print(df2['Age'][0:10])
    print(df2.Age[0:10])
printr(df)
