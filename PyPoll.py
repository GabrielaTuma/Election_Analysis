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

# Initialize vote counter
total_votes = 0

# Declare list of candidates 
candidate_options = []

# Declare a dictionary for candidates/votes
candidate_votes = {}

# Variables to find winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open Input data file
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Header
    headers = next(file_reader)

    # Loop to count rows 
    for row in file_reader:
         # Add total votes count
        total_votes += 1
        
        # Define rows 
        ballot_id = row[0]
        county_name = row[1]
        candidate_name = row[2]

        # Add candidate name to list (without repeating names)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Start tracking candidate vote count 
            candidate_votes[candidate_name] = 0

        # Count votes out of the if statement (all rows)
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    # Write Election Results 
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")

    print(election_results, end=" ")
    txt_file.write(election_results)

    # Loop to find votes per candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes)*100

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


    # Print the winning candidate summary
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
        
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)




     

     
