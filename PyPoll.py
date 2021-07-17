# The data we need to retrieve

# 1. The total number of votes 

# 2. A complete list of cadidates who received votes 

# 3. The percentage of votes each cantidate won

# 4. The total number of votes each candidate won 

# 5. The winner of the election based on popular vote 

# Dependencies
import csv
import os 

# Input
file_to_load = os.path.join("Resources", "election_results.csv")
# Output 
file_to_save = os.path.join("analysis", "elections_analysis.txt")

# Open Input data file
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Header
    headers = next(file_reader)
    print(headers)



