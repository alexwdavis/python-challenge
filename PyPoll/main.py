import pandas as pd
from pathlib import Path

poll_data = pd.read_csv("Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv", encoding="ISO-8859-1", delimiter=",")
poll_data_count = poll_data['Voter ID']
voter_count =len(poll_data_count.value_counts())
#Khan
print_voter_count = "Total Votes: " + str(voter_count) 
only_khan = poll_data.loc[poll_data["Candidate"] == "Khan", :]
khan_total = len(only_khan)
khan_percentage = "{0:.3f}%".format((khan_total / voter_count) * 100)
print_khan = "Khan: " + str(khan_percentage) + "("+ str(khan_total)+ ")"
#Correy
only_correy = poll_data.loc[poll_data["Candidate"] == "Correy", :]
correy_total = len(only_correy)
correy_percentage = "{0:.3f}%".format((correy_total / voter_count) * 100)
print_correy = "Correy: " + str(correy_percentage) + "("+ str(correy_total)+ ")"
#Li
only_li = poll_data.loc[poll_data["Candidate"] == "Li", :]
li_total = len(only_li)
li_percentage = "{0:.3f}%".format((li_total / voter_count) * 100)
print_li = "Li: " + str(li_percentage) + "("+ str(li_total)+ ")"
#O'Tooley
only_otooley = poll_data.loc[poll_data["Candidate"] == "O'Tooley", :]
otooley_total = len(only_otooley)
otooley_percentage = "{0:.3f}%".format((otooley_total / voter_count) * 100)
print_otooley = "O'Tooley: " + str(otooley_percentage) + "("+ str(otooley_total)+ ")"
#Winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_total, correy_total, li_total, otooley_total]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
print_winner = "Winner: " + (key)

print("Election Results")
print("-------------------------")
print(print_voter_count) 
print("-------------------------")
print(print_khan) 
print(print_correy)
print(print_li)
print(print_otooley)
print("-------------------------")
print(print_winner)
print("-------------------------")

total_file = ("Election Results.txt")

with open(total_file,"w",) as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(print_voter_count) 
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(print_khan)
    file.write("\n")
    file.write(print_correy)
    file.write("\n")
    file.write(print_li)
    file.write("\n")
    file.write(print_otooley)
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(print_winner)
    file.write("\n")
    file.write("-------------------------")