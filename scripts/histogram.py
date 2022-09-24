import pandas as pd
import sys
from matplotlib import pyplot as plt

n = 1 

if sys.argv[:1] == "-f":
    n = str((column_selection[2]))


data = pd.read_csv(sys.argv[2], sep='\t', header=0)
# data = pd.read_csv('expres.anal.csv', sep='\t', header=0)
data.head()
df = pd.DataFrame(data)
cols = [1,2,3,4]
df = df[int(df.columns[n])]
ax = df.plot.hist()                     

                        
