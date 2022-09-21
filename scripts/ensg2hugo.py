import re
import sys
# import gffutils
##I considered using gffutils but it's a little complex to extract specific column out

# Create a dictionary searching for ensg genes


gene = "Homo_sapiens.GRCh37.75.gtf"
File = str(sys.argv[1]) # convert the testing file into string

# if inputFile[:2] == "-f":
#     col = int(inputFile[-1])
#     inputFile = str(sys.argv[2])

ENSG = {}
with open(gene) as g:
  for line in g:
    for match in re.findall(r' gene_id\s\"(\S+)\"\;.gene_name\s\"(\S+)\"\;', line): 
      #now we have matched ensg name and hugo name in two groups, we can add them into dictionary
      ENSG [match[0]] = match [1]
   
  
  ##now we have created a dictionary matching all ENSG2HUGO, next step is to apply the dictionary to the source file to replace Ensembl to Hugo
  ###to be continued and edited by Friday                          
                            
                          
    



