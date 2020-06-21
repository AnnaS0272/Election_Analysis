#The Data we need to retrive
# 1. Get the total votes cast for the election.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes cast for each candidate.

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

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# County options and county votes.
county_options = []
county_votes = {}


# Track the winning county, vote count, and percentage.
winning_county = ""
winning_count_county = 0

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.   
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate and county name from each row.
        county_name = row[1]
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1 
        # If the county does not match any existing county,
        # add the county to the county list. 
        if county_name not in county_options:
            # Add the county to the county list
            county_options.append(county_name)
            # And begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to county count. In this dictiionary County is a key, Vote i a value.
        county_votes[county_name] += 1
print(county_votes)
#print(county_options)
#print(candidate_options)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n"
        f"\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file
        txt_file.write(county_results)
        # Determine winning vote count and winning county.
        if (votes > winning_count_county):
            winning_count_county = votes
            winning_county = county    
    # Print the winning candidate's results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest county turnaround: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage_candidate = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage_candidate:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count_candidate) and (vote_percentage_candidate > winning_percentage_candidate):
            winning_count_candidate = votes
            winning_candidate = candidate
            winning_percentage_candidate = vote_percentage_candidate
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"Winning Percentage: {winning_percentage_candidate:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)