##Q1 extract phone number
import re
import sys
file = open('mytextfile.txt','r')
text = file.read()

# print (text)

pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

extract = re.findall(pattern, text)

# print (extract)

for s in extract:   
    if s.split('-')[0]=='+1':        
        l = s.split('-')
        # print (l)
        ls = []
        for i in range(len(l)):
            if i==1:
                ls.append(" (")
                ls.append(l[i])
            elif i==2:
                ls.append(") ")
                ls.append(l[i])
            else:
                ls.append(l[i])   
                
        final = "".join(map(str,ls))      
    else:    
        l = s.split('-')
        # print (l)
        ls = []
        for i in range(len(l)):
            if i==1:
                ls.append(" (")
                ls.append(l[i])
            elif i==2:
                ls.append(") ")
                ls.append(l[i])
            else:
                ls.append(l[i])
                
        final = "".join(map(str,ls))
             
    print(final)

        
        
