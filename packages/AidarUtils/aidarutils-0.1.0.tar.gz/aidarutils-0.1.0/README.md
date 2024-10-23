## 'AidarUtils' is a command-line utility designed to simplify working with CSV, JSON, and TXT files. This versatile tool empowers you to:
###
### • Count the number of characters, lines, and words in a .txt file.
### • Merge the contents of two .txt files, finding the intersection of their elements.
### • Remove duplicates and sort the results of merging and intersection alphabetically for easier data analysis.
### • Filter data within a .json file and then convert it to .csv file.
###
## Installation:

    pip install AidarUtils

## Usage:
    
### Merge 2 .txt files:
    python -m setutils --union list1.txt list2.txt

### Intersect 2 .txt files:
    python -m setutils --intersect list1.txt list2.txt

### Remove duplicates and sort:
    python -m setutils --union list1.txt list2.txt --unique --sort

### .json to .csv conversion with output file name specification:
    python -m json2csv --convert products.json --output products.csv

### Filtering products by price in .json before converting to .csv:
    python -m json2csv --convert products.json --output products.csv --min 10 --max 100

### Filtering data by fields "Category" and "Inventory Status":
    python -m json2csv --convert products.json --output products.csv --category electronics --stock