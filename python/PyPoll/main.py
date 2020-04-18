import os
import csv

pypoll_csv_path = os.path.dirname(__file__) + '/Resources/election_data.csv'

total_votes_cast = 0
candidates = []
vote_counts = []
percentage = []

with open(pypoll_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

#* The total number of votes cast
    for row in csv_reader:
        total_votes_cast += 1
        
    #* A complete list of candidates who received votes    
        candidate = row[2]
        if not candidate in candidates:
            candidates.append(candidate)
            vote_counts.append(1)
        else:
            index = candidates.index(row[2])
            vote_counts[index] +=1
   
    #* The percentage of votes each candidate won  
    for vote in vote_counts:

        percent_votes = (vote/total_votes_cast)
        percentage_votes = (format(percent_votes, "%"))
        percentage.append(percentage_votes)

    #* The total number of votes each candidate won   
    #* The winner of the election based on popular vote.
    max_vote = max(vote_counts)
    index_vote = vote_counts.index(max_vote)
    winner = candidates[index_vote]

print("Election Results")
print("------------------------------------------")
print(f'Total Votes: {total_votes_cast}')
print("------------------------------------------")
print(candidates[0], percentage[0], vote_counts[0])
print(candidates[1], percentage[1], vote_counts[1])
print(candidates[2], percentage[2], vote_counts[2])
print(candidates[3], percentage[3], vote_counts[3])
print("------------------------------------------")
print(f'Winner: {winner}')