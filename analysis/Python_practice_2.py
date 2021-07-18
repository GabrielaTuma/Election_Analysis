counties = ["Arapahoe" , "Denver" , "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


temperature = str(input("What's the temperature outside?"))
if temperature > 80:
    print ("Turn on the AC")
    else print ("Open the windows")

# Whats the score?
score = int(input("What is yout test score?"))

# Determine the grade 
if score >= 90:
    print ("Grade: A")
elif score >= 80:
    print ("Grade B")
elif socre >=70:
    print ("Grade C")
elif score >= 60:
    print ("Grade D")
else print ("Grade F")

if "Arapahoe" in counties:
    print ("True")
    else print ("False")

if "El paso" not in counties:
    print ("True")
    else print ("False")

# Usind AND, OR and NOT
if not "El paso" and "Denver" in counties:
    print ("Yay")

print ("Hello World")
# How many votes did yiu get?
my_votes = int(input("How many votes did you get in the election?"))
# Total votes in the election
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received # percentage_votes = (my_votes/total_votes)*100
print ("I received" + str((percentage_votes) + "% of the total votes")

for county, voters in counties_dict.items():
    print(county, voters)


import datetime
now = datetime.datetime.now()
print ("The time is", now)

import datetime as dt
now = dt.datetime.now()
print ("The time is", now )

# Open the election results and read the file
file_election = 'election_results.csv'
election_data = open(file_election, "r")
election_data.close()

# Dependencies
import csv
import os 

# Open the election results and read the file
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print (election_data)

# Write data in the file 
file_to_save = os.path.join("analysis", "elections_analysis.txt")
with open(file_to_save, "w") as outfile:
    outfile.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

outfile.close()


  # Print each row 
    for row in file_reader:
        print(row[0])
        

# Put total_votes = 0 before ('open' argument)
    # Rows
    for row in file_reader:
        # Add total votes count
        total_votes += 1

print(total_votes)