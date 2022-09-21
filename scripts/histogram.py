import sys
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##from matplotlib.ticker import StrMethodFormatter


with open(file) as f:
   #check if the first column presents by adding an argv: isFirst=True
  for line in f:
    match = re.findall (r'("(\S+)\s", line))[0]
                        
    data.append(match)
                        
#check if the source file can be printed directly
df = pd.read_csv('data')
print(df.shape)                       

                        
