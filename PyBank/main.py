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

    # Create variables to store data
    count_months = 0
    total_prof = []
    monthly_change = []
    date = []

    for row in csvreader:
        # Add up the total number of months in the dataset
        count_months = count_months + 1
        
        # Add up the net total amount of "Profit/Loss" over the period
        total_prof.append(int(row[1]))

        # Calculate the change from the prior month (current row) - (previous row)
        x = (len(total_prof)-1)
        monthly_change.append(total_prof[x]-total_prof[x-1])

        # Append the date
        date.append(row[0])

# Find the greatest increase in profits (date and amount) over the period
# This will be the MAX value of the output of monthly_change code above
max_inc = max(monthly_change)

# Find the greatest decrease i profits (date and amount) over the period
# This will be the MIN value of the output of monthly_change code above
max_dec = min(monthly_change)

max_inc_date = date[monthly_change.index(max_inc)]
max_dec_date = date[monthly_change.index(max_dec)]

# Print the following in the terminal
# Print title "Financial Analysis"
print("Financial Analysis")

# Print "-----------------------" separator
print("-----------------------------")

# Pring Total Months, Total P/L, Average Change, Greatest Inc (date/amt), Greated Dec (data/amt)
print(f'Total Months: {(count_months)}')
print(f'Total: ${int(sum(total_prof))}')
print(f'Average Change: ${sum(monthly_change)/((count_months)-1):.2f}')
print(f'Greatest Increase in Profits:  {max_inc_date} (${max(monthly_change)})')
print(f'Greatest Decrease in Profit: {max_dec_date} (${min(monthly_change)})')
        
# Write the analysis results to a text file
# Set variable for the output file
pybank_output = os.path.join("Analysis", "pybank_analysis.txt")

# Open the output file
with open(pybank_output, "w") as datafile:

    # Write the following to the output text file
    # Write title "Financial Analysis"
    datafile.write("Financial Analysis")

    # Write "-----------------------" separator
    datafile.write("\n-----------------------------\n")

    # Write Total Months, Total P/L, Average Change, Greatest Inc (date/amt), Greated Dec (data/amt)
    datafile.write(f'Total Months: {(count_months)}\n')
    datafile.write(f'Total: ${int(sum(total_prof))}\n')
    datafile.write(f'Average Change: ${sum(monthly_change)/((count_months)-1):.2f}\n')
    datafile.write(f'Greatest Increase in Profits:  {max_inc_date} (${max(monthly_change)})\n')
    datafile.write(f'Greatest Decrease in Profit: {max_dec_date} (${min(monthly_change)})\n')



