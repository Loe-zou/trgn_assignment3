# *trgn_assignment3*

> This readme file is created on the github directly. 
  Three source scripts can be found in the file called *scripts* in the repository.



**Three scripts of the assignment is listed and described below:**


# 1. extract_phonenum.py

## Usage

```
python3 extract_phonenum.py mytextfile.txt
```

## Description

Extracts phone number from a specific text called *mytextfile.txt* and prints the formated phone number.

The phone number is reformatted as [+][country code] ([AreaCode]) [local phone number].

## Known Issues

- Can only test the file named *mytextfile.txt*
- It takes hyphon as space delimiter to group and reformat the number, therefore the phone numbers without hyphen delimited will be unable to be reformated
- For now only the second set of number will be bracketed, so for domestic one without country number the round bracketed number might be off-target

# 2. ensg2hugo.py

## Usage
```
python3 ensg2hugo.py [-f][0-9] [file]
```

## Description

This python program allows you to replace all Ensembl gene name into HUGO name in a given file! Please specify the column for Ensembl within the file using -f[0-9] 

>[0-9] indicated the column number


## Dependencies(What you need)

1. Download and unzip the target file:

```
wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
```
2. Unzip the file `gunzip Homo_sapiens.GRCh37.75.gtf.gz`
3. Unit test file called 'expres.anal.csv' found on ``git clone https://github.com/davcraig75/unit``
  - or instead, gunzip the file within scripts called `expression_results.csv.zip`
4. cd to the source file 'unit' and move it to the assignment 4 directory 
   ``mv expres.anal.csv ~/trgn510_assignment4/scripts``

## Known Issues (updated Sep21)
- ##now we have created a dictionary matching all ENSG2HUGO, next step is to apply the dictionary to the source file to replace Ensembl to Hugo
  ##to be continued and edited by Friday 
- might occur a prob calling out the file, to be tested on the server and git clone
- TBC

# 3. histogram.py
## Usage
```python3 histogram.py [-f][0-9] [file]```

## Description
Creates a histogram as a png from a file using the specified column in a tab delimited file.

## Hypothetical Example
- Can use the same one `expression_results.csv.zip` within the same direcotry 'scripts'

## Known Issues
- Current Logic as follows: (file just created)
- Import and use pandas 
- `pip install pandas` or `pip3 install pandas`
- also `pip install numpy` or `pip3 install numpy`
- please see the source file named `histogram.py` in `scripts`

### edited on Sept 20, 2021
### contact me if u have questions at 
```
zoul@usc.edu
```
###Thanks :)
