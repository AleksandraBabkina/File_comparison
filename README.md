# File_comparison
## Description
This script is designed to automate the process of comparing regular reporting files. It can handle Excel files containing data from different periods, identifying unique and common entries between them. The script helps streamline the comparison process, ensuring that changes between files are accurately detected. By automating this task, it reduces the time and effort required to manually compare reports, improving the efficiency and accuracy of financial or insurance reporting.

## Functional Description
The program performs the following steps:
1. Retrieves two Excel files for comparison.
2. Reads the data from both files into dataframes.
3. Compares the rows of the two files to find unique entries in each.
4. Outputs the unique rows from both files into a new Excel file for further inspection.

## How It Works
1. The program loads two Excel files from a specified folder.
2. The data from the files is read and indexed.
3. It identifies unique rows in each file by comparing the data.
4. The results are written into a new Excel file, containing only the rows that are unique to each file.

## Input Structure
To run the program, the following parameters need to be provided:
1. The path to the folder containing the Excel files to compare.
2. The two Excel files to be compared (must be in the specified folder).

## Technical Requirements
To run the program, the following are required:
1. Python 3.x
2. Installed libraries: pandas, os
3. Two Excel files containing the data to be compared.

## Usage
1. Place the Excel files you wish to compare in the specified folder.
2. Run the script. It will:
    - Read the files.
    - Compare their content.
    - Output a new Excel file with the unique rows from both files.

## Example Output
The output file will contain the unique rows from both files. These rows will be separated and saved for further analysis.

## Conclusion
This script is useful for automating the comparison of regular reporting files, helping you detect changes and unique entries more efficiently. It is a valuable tool for financial, insurance, and other types of reporting where periodic comparisons of data are necessary.
