# python-challenge
Analyze banking and election data with Python scripts

## Background

Python was used to analysis data for 2 projects: PyBank (financial data) and PyPoll (election results). The output of the script created an analysis summary table for each and a text file output.

### Approach

PyBank:
- Leveraged Python scrips to loop through 86 months profit/loss data
- "For Loops” where employed to iterate through the data and perform various calculations
- Conditional arguments were used to determine:
    * the largest monthly increase in profit with corresponding date
    * the largest monthly decrease in profit with corresponding date

PyPoll:
- Leveraged Python scrips to loop through 360,000 ballots to determine the following: 
    * Total Ballots Cast
    * Unique Candidates Receiving Votes
    * Candidate Name with Percent of Votes and Total Votes Received
    * Overall Winning Candidate
    
#### Files Used for Data Analysis
budget_data.csv
election_data.csv

##### References & Resources
https://devenum.com/pandas-sum-columns-by-multiple-conditions/
https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html
https://www.analyseup.com/learn-python-for-data-science/python-pandas-add-new-column-to-dataframe.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html
https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/
https://towardsdatascience.com/different-ways-to-create-subset-and-combine-dataframes-using-pandas-e7227330a7f1
