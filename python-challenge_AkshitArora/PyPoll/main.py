import os
import csv

total_votes=0
winner_vote=0
winner=""
candidates=[]
vote_counter={}
vote_percentage=[]
max_vote=0

csvpath=os.path.join("..", "Resources", "election_data.csv")

with open (csvpath, newline="") as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
        candidate=row[2]
        
        if candidate in candidates:
            vote_counter[candidate]+=1
        else:
            candidates.append(candidate)
            vote_counter[candidate]=1
        total_votes+=1

for i in range(len(candidates)):
	vote_share = round((vote_counter[candidates[i]]/total_votes)*100, 3)
	vote_percentage.append(vote_share)
	if vote_counter[candidates[i]] > max_vote:
		max_vote = vote_counter[candidates[i]]
		winner = candidates[i]

print("Election Results")
print("-------------------------------------")
print(f'Total Votes:{total_votes}')
print("-------------------------------------")
for i in range(len(candidates)):
	print(f'{candidates[i]} : {vote_percentage[i]} % ( {vote_counter[candidates[i]]})')
print("-------------------------------------")
print(f'Winner: {winner}')
print("------------------------------------- ")


output= open("Election Results.txt","w+")
output.write("Election Results \n")
output.write("------------------------------------- \n")
output.write(f'Total Votes: {total_votes} \n')
output.write("------------------------------------- \n")
for i in range(len(candidates)):
	output.write(f'{(candidates[i])} : {(vote_percentage[i])} % {vote_counter[candidates[i]]} \n')
output.write("------------------------------------- \n")
output.write(f'Winner: {winner}' + "\n")
output.write("------------------------------------- \n")
output.close()