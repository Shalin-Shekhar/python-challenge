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

print(F'Election Results',file = output_file)
print(F'-------------------------',file = output_file)
print(F'Total Votes: {}',file = output_file)
print(F'-------------------------',file = output_file)  

for candidate in candidates:
    votes_list = [vote for vote in votes if vote == candidate]
    print(F'{candidate}: {round(float(((len(votes_list))/total_votes) * 100),3)}% ({int(len(votes_list))})',file = output_file)


#print(F'Election Results')
#print(F'-------------------------')
#print(F'Total Votes: {}')
#print(F'-------------------------')
#print(F'{}: {}% ({})')
#print(F'{}: {}% ({})')
#print(F'{}: {}% ({})')
#print(F'{}: {}% ({})')
print(F'-------------------------',file = output_file)
print(F'Winner: {}')
print(F'-------------------------',file = output_file)

# Set variable for output file
#output_file = open("Election Results.txt","a") 

# write to the file
#print(F'',file = output_file)

# Closing a file "output_file.txt" 
output_file.close()