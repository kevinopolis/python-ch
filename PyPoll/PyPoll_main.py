
# Import Dependancies
import os
import csv

# DecVAr
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

# file input
csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

# Read the File
with open(csvpath, newline = "") as poll_data:
    csvreader = csv.reader(poll_data, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        #total vote count
        total_votes += 1
        #candidates & count
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # calculate percentages
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        # declare winner
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]
# output file
file_output = os.path.join('..','PyPoll', 'Resources', 'poll_output.text')

# writing to utput file
with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")
