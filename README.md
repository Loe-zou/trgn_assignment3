# *trgn_assignment3*

> This readme file is created on the github directly. 
  Three source scripts can be found in the file called *scripts* in the repository.

*remember to `git clone Loe-zou/trgn_assignment3` first to get all the documents to be tested on the server.*

**Three scripts of the assignment is listed and described below:**


# 1. extract_phonenum.py

## Usage

```
python3 extract_phonenum.py [file]
```

> feel free to use ```mytextfile.txt``` attached in this repository to test out the '''[file]```

## Description

Extracts phone number from a specific text called *mytextfile.txt* and prints the formated phone number.

The phone number is reformatted as [+][country code] ([AreaCode]) [local phone number].

## Known Issues

- It takes hyphon as space delimiter to group and reformat the number, therefore the phone numbers without hyphen delimited will be unable to be reformated
- For now only the second set of number will be bracketed, so for domestic one without country number the round bracketed number might be off-target

# 2. ensg2hugo.py

## Usage
```
python3 ensg2hugo.py [-f][0-9] [file] on the server
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
5. The unit test run file `expression_results.tsv` is already placed in the `scripts`

## Known Issues (updated Oct 31)
- The dictionary works, can test it out by uncommenting `print (ENSG)` ;
- The column has to be no bigger than 9, and column 0 will be converted to the last column;
- The end output is a list, can be appended to a new tsv file seperately (or simply copy and paste).

# 3. histogram.py
## Usage
```python3 histogram.py [-f][0-9] [file]```

## Description
Creates a histogram as a png from a file using the specified column in a *tab delimited* file.

## Hypothetical Example
- Can use the same one `expression_results.tsv` within the same direcotry 'scripts'

## Known Issues
- The column selection is limited within 9, and need to make sure the column has floats or numerics only;
- Works fine on tsv, need to replace "\t" to "," to cope with csv plotting.


### edited on Oct 31, 2022
### contact me if u have questions at 
```
zoul@usc.edu
```
###Thanks :)
