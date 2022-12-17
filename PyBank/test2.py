# Import module os to create file paths across operating systems
import os

# Import module csv for reading CSV files
import csv

# Point to path of csvfile
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifices delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    #create empty lists to add the csv values to 
    count_month = []
 
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        count_month.append(row[0])


print(f"Total Months:{len(count_month)}")
