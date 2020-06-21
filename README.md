# Election Analysis

## Project Overview
A Colorado Board of Elections employee Tom has asked for help with election audit with recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.8.1, Visual Studio Code 1.46.0

## Summary

The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 of votes.
- The winner of the election was:
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  
## Challenge Overview

The election commission also requested to confirm the voter turnout for each county. In this challenge, it is required to determine the number of votes that were cast from each county and the percentage of votes each county contributed to the election.

## Challenge Summary

In order to complete the task, I created an additional dictionary for counties with key as county and value as number of votes. 

```
county_options = []
county_votes = {}
```
I then added one more `If` statement into our main loop to perform similar iteration we performed for candidates but for the second dimension, i.e., ***county***. 

Once our dictionaries are populated with unique values for counties and total count of votes, we can determine which county is the winning county and write the results into a text file as follows:

```
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
```




