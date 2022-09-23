import re
import sys
# import pandas as pd
# import numpy as np


# Create a dictionary searching for ensg genes


gene = "Homo_sapiens.GRCh37.75.gtf"
File = str(sys.argv[1]) ##convert the testing file into string from the first argument

if File[:2] == "-f":
    col = int(File[-1]) ##minus one due to index, now col becomes the target column number
    File = sys.argv[2]
else:
    col = 1
    File = sys.argv[1] ##if -f is missing

ENSG = {}
with open(gene) as file:
    for line in file:
          ensg = re.findall(r'ENSG\d{11,}', line, re.I)
          hugo = re.findall(r'gene_name\s\"(\S+)\"', line, re.I)
          if ensg:
              if hugo:
                  ENSG [ensg[0]]=hugo[0]
                  #print (ENSG)
                    
# Extract lines from source File and append to a new lines list where ENSG is replaced into HUGO

new_list = []

with open (File, 'r') as F:
    #append header
    first_line = F.readline()
    new_list.append(first_line)
    
    for line in F:
        ensg = line.split(",")
        matches = re.match(r'\"(\S*?).\S*?\", ensg[col])
        if matches:
                           
  
  
    
  
      
    
     
      

    
                          
    



