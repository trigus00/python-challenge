import os

import csv



election_data_path = os.path.join('/Users/gmendoza/Documents/GitHub/python-challenge/PyRoll/main.py','election_data.csv')
with open('election_data.csv', newline='') as csvfile:
    
    total_votes = 0 
    candidate = ""
    candidate_votes= {}
    winner_name = 0
    winner = ""
    candidate_percent = {}
    
   

    vote = csv.DictReader(csvfile)
    
   
    
    for row in vote:

        total_votes = total_votes + 1 
        candidate = (row['Candidate'])
        
        if candidate in candidate_votes: 
             candidate_votes[candidate] += 1 
        else:
             candidate_votes[candidate] = 1
     
for name, vote_count in candidate_votes.items():
     candidate_percent[name] = '{0:.0%}'.format(vote_count / total_votes)
     if vote_count > winner_name:
         winner_name = vote_count
         winner = name
   
          



print (" -----Election Results----- \n")
print (f"Total Votes : {total_votes}\n")

print(f"{name}")
for candidate in candidate_votes:
    print (f"Percent of each candidate: {candidate} {candidate_percent[candidate]}\n" )
    print (f"Vote Count : {vote_count}")
print (f"Winner: {winner}\n")

