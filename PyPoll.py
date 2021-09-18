# Import CSV and OS Module
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Declaring total votes variable to count
total_votes = 0

# Declare candidate list
candidate_options = []

# Declare empty  Dictionary to hold candidate name and their votes count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print header from csv file
    header = next(file_reader)
    #print(header)

    # Print each row in the csv file
    for row in file_reader:
        #print(row)

        # Add to the total variable
        total_votes += 1

        # Print candidate name from each row
        candidate_name =row[2]

        # if the candidate dose not match any existing candidate
        if candidate_name not in candidate_options:

        # Add candidate name to the candidate list
            candidate_options.append(candidate_name)

        # Tracking candidate vote count    
            candidate_votes[candidate_name] = 0
        
        # Add a vote to candidate counts
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file: 
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
# Save the final vote count to the text file.
    
    txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.    
        #txt_file.write(candidate_results)

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # print candidate name
    #print(candidate_options)

    # Print the candidate vote dictionary.
    #print(candidate_votes)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    #print(f"Total Number of Votes {total_votes : ,}")