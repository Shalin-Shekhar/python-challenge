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
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Lists to store data
date = []
pnl = []
revenue = 0
total_mnths = 0
total_amt = 0
max_profit = 0
profit_year = ""
max_loss = 0
loss_year = ""
avg_amt = 0


# Open file to read
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Identify the header
    header = next(csvreader)

    for row in csvreader:
        # Add Date
        date.append(row[0])
        # Add price
        pnl.append(float(row[1]))
        total_amt += int(row[1])
        revenue = int(row[1])

        if revenue > max_profit:
            max_profit = revenue
            profit_year = row[0]
        
        if revenue < max_loss:
            max_loss = revenue
            loss_year = row[0]

    # do all the work on data
    total_mnths = len(date)
    avg_amt = average(pnl)

    print(F'Financial Analysis')
    print(F'----------------------------')
    print(F'Total Months: {total_mnths}')
    print(F'Total: ${total_amt}')
    print(F'Average Change: ${avg_amt}')
    print(F'Greatest Increase in Profits: {profit_year} (${max_profit})')
    print(F'Greatest Decrease in Profits: {loss_year} (${max_loss})')
# Set variable for output file
output_file = open("Financial Analysis.txt","a") 

# write to the file
print(F'Financial Analysis',file = output_file)
print(F'----------------------------',file = output_file)
print(F'Total Months: {total_mnths}',file = output_file)
print(F'Total: ${total_amt}',file = output_file)
print(F'Average Change: ${avg_amt}',file = output_file)
print(F'Greatest Increase in Profits: {profit_year} (${max_profit})',file = output_file)
print(F'Greatest Decrease in Profits: {loss_year} (${max_loss})',file = output_file)

# Closing a file "output_file.txt" 
output_file.close()