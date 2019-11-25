# First we'll import the os and csv module
# This will allow us to create file paths across operating systems
import os
import csv

# Write a function that returns unique list
def unique(InputList):
    uq_list = []
    for name in InputList:
        if name not in uq_list:
            uq_list.append(name)        
    return uq_list

# Create a CSV file handler
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Lists to store data
candidates = []
voter = []
votes = []
total_votes = 0
votes_list = []
votes_per_candidate = []


# Open file to read
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Identify the header
    header = next(csvreader)

    for row in csvreader:
        # Add Candidates
        votes.append(row[2])
        # Add votes
        voter.append(row[0])

    # do all the work on data
    total_votes = int(len(voter))
    candidates = unique(votes)

# Set variable for output file
output_file = open("Election Results.txt","a") 

print(F'Election Results')
print(F'-------------------------')
print(F'Total Votes: {total_votes}')
print(F'-------------------------')  
print(F'Election Results',file = output_file)
print(F'-------------------------',file = output_file)
print(F'Total Votes: {total_votes}',file = output_file)
print(F'-------------------------',file = output_file)

# Sum the votes for every candidate
for candidate in candidates:
    votes_list = [vote for vote in votes if vote == candidate]
    votes_per_candidate.append(round(float(((len(votes_list))/total_votes) * 100),3))
    print(F'{candidate}: {round(float(((len(votes_list))/total_votes) * 100),3)}% ({int(len(votes_list))})',file = output_file)
    print(F'{candidate}: {round(float(((len(votes_list))/total_votes) * 100),3)}% ({int(len(votes_list))})')

# Find the winner of the election
idx = votes_per_candidate.index(max(votes_per_candidate))
print(F'-------------------------')
print(F'Winner: {candidates[idx]}')
print(F'-------------------------')
print(F'-------------------------',file = output_file)
print(F'Winner: {candidates[idx]}',file = output_file)
print(F'-------------------------',file = output_file)

# Closing a file "output_file.txt" 
output_file.close()
