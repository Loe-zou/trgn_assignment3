#!/usr/bin/python
import re
import sys
import fileinput
# import pandas as pd
# import numpy as np
#pandas dataframe is quicker but decided to use the tranditional way


### Create a dictionary searching for ensg genes

gene = "Homo_sapiens.GRCh37.75.gtf"

ENSG = {}
with open(gene) as file:
    for line in file:
          ensg = re.findall(r'ENSG\d{11,}', line, re.I)
          hugo = re.findall(r'gene_name\s\"(\S+)\"', line, re.I)
          if ensg:
              if hugo:
                  ENSG [ensg[0]]=hugo[0]
                  #print (ENSG)
                    #Test point here - dictionary check
                
                
###Match and replace  

File = str(sys.argv[1]) ##convert the testing file into string from the first argument

if File[:2] == "-f":
    col = int(File[-1]) ##minus one due to index, now col becomes the target column number
    File = sys.argv[2]
else:
    col = 1
    File = sys.argv[1] ##if -f is missing
    
with open(File) as f:
    First = True
    for line in f:
        if not First:
            split = line.split(",") #for csv only, not tsv
            match = re.findall("([^,]+),", line)[col - 1]
            match = re.findall("[^\"\s]+", match)[0]
            Sub = re.findall("[^\.]+", match)[0]         #find all ensg matches in the column, this ensures multiple appearance can be matched as well
            split[col - 1] = split[col - 1].replace(match, ENSG.get(Sub, match)) #substituted according to the dictionary on line 22
            line = ",".join(split)
        First = False    
            
        print(line) #print the result into a list, can be appended to a tsv file as well
      

    
                          
    



