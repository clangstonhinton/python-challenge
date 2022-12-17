# Import module os to create file paths across operating systems
import os

# Import module csv for reading CSV files
import csv

# Import statistics module
import statistics

# Point to path of csvfile
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifices delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Create variables to store list data 
    count_months = []
    total_prof = []
    monthly_change = []

    for row in csvreader:
        # Add up the total number of months in the dataset
        count_months.append(row[0])
        # Add up the net total amount of "Profit/Loss" over the period
        total_prof.append(int(row[1]))
        # Calculate the change from the prior month (current row +1) - (current row)
    
        x = (len(total_prof)-1)
        monthly_change.append(total_prof[x]-total_prof[x-1])

# Find the greatest increase in profits (date and amount) over the period
# This will be the MAX value of the output of Row 13 in code above
max_inc = max(monthly_change)

# Find the greatest decrease i profits (date and amount) over the period
# This will be the MIN value of the output of Row 13 in code above
max_dec = min(monthly_change)

x = len(monthly_change)


# Print the following in the terminal
# Write title "Financial Analysis"
print("Financial Analysis")

# Write "-----------------------" separator
print("-----------------------------")

# Write Total Months, Total P/L, Average Change, Greatest Inc (date/amt), Greated Dec (data/amt)
print(f'Total Months: {len(count_months)}')
print(f'Total: ${int(sum(total_prof))}')
print(f'Total Monthly Change: ${int(sum(monthly_change))}')
print(f'Average Change: ${int(sum(monthly_change)/len(monthly_change))}')
print(f'Greatest Increase in Profits:  ${max(monthly_change)}')
print(f'Greatest Decrease in Profit: ${min(monthly_change)}')
        

# Write the analysis results to a text file
# Set variable for the output file
pybank_output = os.path.join("Analysis", "pybank_analysis.txt")

# Open the output file
#with open(pybank_output, "w") as datafile:

    # Write the following to the output text file
    # Write title "Financial Analysis"
    #datafile.write("Financial Analysis")

    # Write "-----------------------" separator
    #datafile.write("\n-----------------------------")

    # Write Total Months, Total P/L, Average Change, Greatest Inc (date/amt), Greated Dec (data/amt)
    #datafile.write(f'\nTotal Months: {len(count_months)}')
    #datafile.write(f'\nTotal: ${int(sum(total_prof))}')
    #datafile.write(f'\nAverage Change: ${int(sum(monthly_change)/len(monthly_change -1),2)}')
    #datafile.write(f'\nGreatest Increase in Profits: ${max(monthly_change)}')
    #datafile.write(f'\nGreatest Decrease in Profit: ${min(monthly_change)}')

#Calcuate the average monthly change and round it    
    #av_mon_chng = round(sum(changes)/(month_count -1),2)
    

