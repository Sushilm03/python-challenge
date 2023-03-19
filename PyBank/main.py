#import modules
import os
import csv

# Set path for data
csvpath = os.path.join( "Resources", "budget_data.csv")
txtpath = os.path.join( "Analysis", "Financial_Analysis_SM.txt")

# Define Lists
date = []
monthly_pchanges = []
months = 0
total_profit = 0 
starting_profit = 0
profit_change = 0
total_profit_change = 0
max = ["",0]
min = ["",0]

# Open CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #store months and monthly profit changes
    for row in csvreader:
        date.append(row[0])
        monthly_pchanges.append(row[1])

        #calculate number of months
        months += 1
        total_profit += int(row[1])

        #calculate total profit monthly change 
        profit_change = int(row[1]) - starting_profit
        if starting_profit == 0:
            profit_change = 0
        starting_profit = int(row[1])
        total_profit_change += profit_change

        #Calculate Max profit change
        if profit_change > int(max[1]):
            max[1] = profit_change
            max[0] = row[0]

        #Calculate Min profit change
        if profit_change < int(min[1]):
            min[1] = profit_change
            min[0] = row[0]

    #calculate total profit change
    total_profit_change = total_profit_change / (months - 1)


# print Summary
print("#######################################################\n")
print("Financial Analysis\n")
print("#######################################################\n")
print(f"Total Months:  {months}\n")
print(f"Total:  ${total_profit}\n")
print(f"Average Change: ${total_profit_change:.2f}\n")
print(f"Greatest Increase in Profits: {max[0]} (${max[1]})\n")
print(f"Greatest Decrease in Profits: {min[0]} (${min[1]})\n")
print("#######################################################\n")

 # create a text file
with open(txtpath, "w") as result:
    result.write("#######################################################\n")
    result.write("Financial Analysis\n")
    result.write("#######################################################\n")
    result.write(f"Total Months:  {months}\n")
    result.write(f"Total:  ${total_profit}\n")
    result.write(f"Average Change: ${total_profit_change:.2f}\n")
    result.write(f"Greatest Increase in Profits: {max[0]} (${max[1]})\n")
    result.write(f"Greatest Decrease in Profits: {min[0]} (${min[1]})\n")
    result.write("#######################################################\n")