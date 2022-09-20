# trgn_assignment3
This is the third trgn 510 assignment which dues on the week of Sept 19.
This readme file is created on github directly while the scripts and testing files are created on the trgn server and commited from there.

Three scripts of the assignment is listed and denoted as follows:

# 1. extract_phonenum.py
## Usage
python3 extract_phonenum.py mytextfile.txt
## Description
Extracts phone number from a specific text called *mytextfile.txt* and prints the formated phone number
The phone number is reformatted as 
## Known Issues
1.Can't distinguish the number 
2.Needs to get rid of the hyphen
3.The current reformatting number is missing [ ] and ( ) - I am thinking using re.split to regroup each segment of the number and reprint it, but a lot of bugs

# 2. ensg2hugo.py
## Usage
python3 ensg2hugo.py [-f][0-9] [file]
## Description
Mimicing the way how we look up for Ensembl name in Homo_sapiens.GRCh37.75.gtf to be replaced by HUGO name
The way to get Homo_sapiens.GRCh37.75.gtf file: 
wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
unzip it using **gunzip**
## Known Issues


# 3. histogram.py
## Usage
## Description
## Known Issues
