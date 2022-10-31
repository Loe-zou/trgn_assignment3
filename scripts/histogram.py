#!/usr/bin/python

import pandas as pd
import sys
from matplotlib import pyplot as plt

column = 2 

if sys.argv[:1] == "-f":
    n = sys.argv[1]
    column = int(n[2])


data = pd.read_csv(sys.argv[2], sep='\t', header=0)
# data = pd.read_csv('expres.anal.csv', sep='\t', header=0) ##this works on jupyternotebook and prints but not working on server
data.head()


# df = pd.DataFrame(data)
# cols = [1,2,3,4]
# df = df[int(df.columns[n])]

col = data.columns[column]
ax = data.loc[:,col]


plot = df.plot.hist()                     

plt.savefig("histogram.png")
