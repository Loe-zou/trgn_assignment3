#!/usr/bin/python
import pandas as pd
import sys
from matplotlib import pyplot as plt



if "-f" in sys.argv[1]:
    n = sys.argv[1]
    column = int(n[2])
else:
    column = 2

    
#check point
#print(column)

data = pd.read_csv(sys.argv[2], sep='\t', header=0)

#data.head(1)

# df = pd.DataFrame(data)
# cols = [1,2,3,4]
# df = df[int(df.columns[n])]

col = data.columns[column]
ax = data.loc[:,col]

plot = ax.plot.hist()                     

plt.savefig("histogram.png")
