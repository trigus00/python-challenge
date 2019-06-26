import os

import csv

election_data_path = os.path.join('/Users/gmendoza/Documents/GitHub/python-challenge/PyPoll/main.py','election_data.csv')
with open('election_data_path', newline='') as csvfile:
    
    vote = csv.DictReader(csvfile)
    
    for name in vote:
        print (name)