# Import module os to create file paths across operating systems
import os

# Import module csv for reading CSV files
import csv

# Point to path of csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv file
with open(csvpath) as csvfile:

    # CSV reader specifices delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile)

    # Create variables to store data
    total_votes = 0
    candidate_names = {}
    max_votes = 0
    winner = ""

    for row in csvreader:
        # Add up the total number of months in the dataset
        if not row['Candidate'] in candidate_names:
            candidate_names[row['Candidate']] = 1
        else:
            candidate_names[row['Candidate']] += 1
        total_votes = total_votes + 1

# Print the following in the terminal
print("Election Results")

print("-----------------------------")

# Print Total Votes
print(f'Total Votes: {(total_votes)}')

print("-----------------------------")

# print Camdidate Names, % Votes Received, Total Votes Received
for key in candidate_names.keys():
    print(f'{key}: {float(candidate_names[key]/total_votes):.3%} ({candidate_names[key]})')
    if candidate_names[key] > max_votes:
        winner = key
        max_votes = candidate_names[key]

print("-----------------------------")

# print Winner
print(f'Winner: {(winner)}')

print("-----------------------------")


# Set variable for the output file
pypoll_output = os.path.join("Analysis", "pypoll_analysis.txt")

# Open the output file
with open(pypoll_output, "w") as datafile:

    # Write the following to the output text file
    # Write title "Election Results"
    datafile.write("Election Results\n")
    
    datafile.write("-----------------------------\n")
   
    # Write Total Votes
    datafile.write(f'Total Votes: {(total_votes)}\n')
    
    datafile.write("-----------------------------\n")
    
    for key in candidate_names.keys():
        datafile.write(f'{key}: {float(candidate_names[key]/total_votes):.3%} ({candidate_names[key]})\n')
        if candidate_names[key] > max_votes:
            winner = key
        max_votes = candidate_names[key]

    datafile.write("-----------------------------\n")

    datafile.write(f'Winner: {(winner)}')

    datafile.write("\n-----------------------------\n")
