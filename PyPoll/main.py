#import modules
import os
import csv

# Set csv and text file paths
csvpath = os.path.join( 'Resources', 'election_data.csv')
txtpath = os.path.join( "Analysis", "Election_Results_SM.txt")

# Define lists

Candidates = []
Votes = []
County = []
Charles_CS = []
Diana_D = []
Raymon_AD = []

#Read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Store Votes, Candidates and County
    for row in csvreader:
        Votes.append(row[0])
        County.append(row[1])
        Candidates.append(row[2])
        
    # Calculate total votes
        Total_Votes = len(Votes)

        # Calculate total votes by candidate.
for candidate in Candidates:
            if candidate == "Charles Casper Stockham":
                Charles_CS.append(candidate)
            
            elif candidate == "Diana DeGette":
                Diana_D.append(candidate)
            
            else: 
                Raymon_AD.append(candidate)
Total_Votes_For_Diana_D = len(Diana_D)
Total_Votes_For_Charles_CS = len(Charles_CS)
Total_Votes_For_Raymon_AD = len(Raymon_AD)

# Calculate Votes % by candidate.
Percentage_For_Charles_CS = round(((Total_Votes_For_Charles_CS / Total_Votes) * 100), 3)
Percentage_For_Diana_D = round(((Total_Votes_For_Diana_D / Total_Votes) * 100), 3)
Percentage_For_Raymon_AD = round(((Total_Votes_For_Raymon_AD / Total_Votes) * 100), 3)

def winner():
    if (Total_Votes_For_Diana_D > Total_Votes_For_Charles_CS) and (Total_Votes_For_Diana_D > Total_Votes_For_Raymon_AD):
        winner = "Diana DeGette"
    elif (Total_Votes_For_Charles_CS > Total_Votes_For_Raymon_AD) and (Total_Votes_For_Charles_CS > Total_Votes_For_Diana_D):
        winner = "Charles Casper Stockham"
    else:
        winner ="Raymon Anthony Doane"
    return(winner)

#Print Summary
print("################################################################\n")
print("Election Results\n")
print("################################################################\n")
print(f"Total Votes:  {Total_Votes}\n")
print("################################################################\n")
print(f"Charles Casper Stockham: {Percentage_For_Charles_CS}% ({Total_Votes_For_Charles_CS})\n")
print(f"Diana DeGette: {Percentage_For_Diana_D}% ({Total_Votes_For_Diana_D})\n")
print(f"Raymon Anthony Doane: {Percentage_For_Raymon_AD}% ({Total_Votes_For_Raymon_AD})\n")
print("################################################################\n")
print(f"Winner: {winner()}\n")
print("################################################################\n")

# create a text file
with open(txtpath, "w") as result:
    result.write("################################################################\n")
    result.write("Election Results\n")
    result.write("################################################################\n")
    result.write(f"Charles Casper Stockham: {Percentage_For_Charles_CS}% ({Total_Votes_For_Charles_CS})\n")
    result.write(f"Diana DeGette: {Percentage_For_Diana_D}% ({Total_Votes_For_Diana_D})\n")
    result.write(f"Raymon Anthony Doane: {Percentage_For_Raymon_AD}% ({Total_Votes_For_Raymon_AD})\n")
    result.write("################################################################\n")
    result.write(f"Winner: {winner()}\n")
    result.write("################################################################\n")