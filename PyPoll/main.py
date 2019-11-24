# First we'll import the os and csv module
# This will allow us to create file paths across operating systems
import os
import csv

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return round(total / length,2)

# Create a CSV file handler
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Lists to store data


# Open file to read
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Identify the header
    header = next(csvreader)

    for row in csvreader:
        # Add Date
        
        # Add price

    # do all the work on data


    print(F'')

# Set variable for output file
output_file = open("Election Results.txt","a") 

# write to the file
print(F'',file = output_file)

# Closing a file "output_file.txt" 
output_file.close()