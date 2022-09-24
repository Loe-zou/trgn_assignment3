# *trgn_assignment3*

> This readme file is created on the github directly. 
  Three source scripts can be found in the file called *scripts* in the repository.

*remember to `git clone Loe-zou/trgn_assignment3` first to get all the documents to be tested on the server.*

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

## Known Issues (updated Sep21)
- The dictionary works, can test it out by uncommenting `print (ENSG)` ;
- The second part with appending matches (ensg to hugo) into new_list has some indentation errors yet to be found, but the replacement is working by test printing the steps in betweem;
- There might be some indentation errors in the second part upon pasting from jupyter lab, if the test run show the error, `vi ensg2hugo.py` to edit the error line by deleting the redundant indentations, otherwise the replacement should work;
- The end output is a list, might need to print each lines in a for loop but the result is still the same just looks a bit messy for now.

# 3. histogram.py
## Usage
```python3 histogram.py [-f][0-9] [file]```

## Description
Creates a histogram as a png from a file using the specified column in a tab delimited file.

## Hypothetical Example
- Can use the same one `expression_results.tsv` within the same direcotry 'scripts'

## Known Issues
- It works and prints the histogram in the jupyter lab but fails when applying sys.argv on the server
- I will send an email indicating the runable scripts on jupyter and the error bar shown in the terminal, Bigy and I tried entire morning to work it out but still failed


### edited on Sept 20, 2021
### contact me if u have questions at 
```
zoul@usc.edu
```
###Thanks :)
