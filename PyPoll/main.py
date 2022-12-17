# Import module os to create file paths across operating systems
import os

# Import module csv for reading CSV files
import csv


# Point to path of csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifices delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Create variables to store list data 
    total_votes_cast = []
    candidates_list_dup = []
    candidates_unique = []

    for row in csvreader:
        # Add up the total number of votes cast
        total_votes_cast.append(row[0])
        # Add candidate voted for to candidate list
        candidates_list_dup.append(row[2])

    for item in candidates_list_dup:
        if item not in candidates_unique:
            candidates_unique.append(item)


# Print the following in the terminal
# Print title "Election Analysis"
print("Election Results")

# Print "-----------------------" separator
print("-----------------------------")

# Print Total Votes Cast
print(f'Total Votes Cast: {len(total_votes_cast)}')

# Write "-----------------------" separator
print("-----------------------------")

# Print out candidates with votes
for item in candidates_unique: 
    print(item) 

# Write Total Months, Total P/L, Average Change, Greatest Inc (date/amt), Greated Dec (data/amt)
#print(f'Total Months: {len(count_months)}')
#print(f'Total: ${int(sum(total_prof))}')
#print(f'Total Monthly Change: ${int(sum(monthly_change))}')
#print(f'Average Change: ${int(sum(monthly_change)/len(count_months))}')
#print(f'Greatest Increase in Profits:  ${max(monthly_change)}')
#print(f'Greatest Decrease in Profit: ${min(monthly_change)}')
        

# Write the analysis results to a text file
# Set variable for the output file
#pybank_output = os.path.join("Analysis", "pybank_analysis.txt")

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
    

