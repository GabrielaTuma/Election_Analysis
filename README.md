# Election_Analysis
Module 3 - Python

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

- [x] 1. Calculate total number of votes.
- [x] 2. Get a complete list of candidates who received votes.
- [x] 3. Calculate the total number of votes each candidate received.
- [x] 4. Calculate the percentage of votes each candidate won. 
- [x] 5. Determine the winner of the election based on popular vote.

Python file with first analysis: [Analysis by candidate](https://github.com/GabrielaTuma/Election_Analysis/blob/ef5ffe6bbbd90a2cc3d093f665fa8bfc4f267614/PyPoll.py)

## Resources 

- Data Source: [election_results.csv](https://github.com/GabrielaTuma/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.58.1

## Summary 
The analysis of the congressional election starts with sorting the data and simplifying the information. 

1. First we found the total number of votes: **369,711**

2. Then the complete list of candidates that received votes 

**Candidate 1: Charles Casper Stockham**

**Candidate 2: Diana DeGette**

**Candidate 3: Raymon Anthony Doane**


3. By creating a variable for the votes per candidates and their respective (4.) percentage we found the election results by candidate 

**Candidate 1 received 23% of the votes (85,213 of the total)**

**Candidate 2 received 73.8% of the votes (272,892 of the total)**

**Candidate 3 received 3.1% of the votes (11,606 of the total)**


5. The winner of the election based on popular vote is:
**Diana DeGette**
**with 272,892 of the votes, 73.8% of total**

## Challenge Overview

- [x] 1. How many votes were cast in this congressional election?
- [x] 2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- [x] 3. Which county had the largest number of votes?
- [x] 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- [x] 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Python file with second analysis: [Analysis by candidate and county](https://github.com/GabrielaTuma/Election_Analysis/blob/ef5ffe6bbbd90a2cc3d093f665fa8bfc4f267614/PyPoll_Challenge.py)

## Challenge Summary 

1. How many votes were cast? **369,711**

From the counties:

**County 1: Jefferson**

**County 2: Denver**

**County 3: Arapahoe**


2. Breakdown per county

**County 1 received 10.5% of the votes (38,855 of the total)**

**County 2 received 82.8% of the votes (306,055 of the total)**

**County 3 received 6.7% of the votes (24,804 of the total)**


3. The county with the largest number of votes is: **Denver**


4. Breakdown per candidate

**Candidate 1 received 23% of the votes (85,213 of the total)**

**Candidate 2 received 73.8% of the votes (272,892 of the total)**

**Candidate 3 received 3.1% of the votes (11,606 of the total)**


5. The winner of the election based on popular vote is:
**Diana DeGette**
**with 272,892 of the votes, 73.8% of total**


### Purpose 
The election commission has requested some additional data to complete the audit:
- Voter turnout for each county
- Percentage from each county of the total count
- County with the highest turnout

While trying to find the numbers per county something is very clear: **most of the code can be recycled** from the first assignment. 

Different data can be analyzed with the same logical sequences if they have the same purpose - finding the variable 'x' with the biggest 'y' associated in this case 

![Candidate vs County](https://github.com/GabrielaTuma/Election_Analysis/blob/7b935aa1f6a94015581221052939be44551c48e5/analysis/Candidate%20vs%20County%20Analysis%202.png)

Comparing codes for candidate and county analysis

![Comparing codes](https://github.com/GabrielaTuma/Election_Analysis/blob/7b935aa1f6a94015581221052939be44551c48e5/analysis/Candidate%20vs%20County%20Analysis%20.png)

Even though we are analyzing different variables: candidate and county, our goal is the same, finding a 'winner' with the biggest amount of votes. The script can be used for any election by doing small adjustments to the code. 

If the winner of the election needs to have more than 50% of the total votes, for example, new lines need to be added to our script. But for most of the situations where we need to find the most voted variable we can recycle this code and save a lot of time and energy. 


