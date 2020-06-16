#The Data we need to retrive
# 1. Get the total votes cast for the election.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes cast for each candidate.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    print(election_data)
    #file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

