import os
import csv
from itertools import count

input_file = os.path.join("PyPoll/Resources/election_data.csv")
output_file = os.path.join("PyPoll/analysis/election_analysis.txt")


with open(input_file) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    data = list(reader)
    row_count = len(data)

    candidates_list = list()
    tally = list()
    for i in range(0, row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidates_list:
            candidates_list.append(candidate)
    candicount = len(candidates_list)

    votes = list()
    percentage = list()
    for s in range(0, candicount):
        name = candidates_list[s]
        votes.append(tally.count(name))
        vprct = votes[s]/row_count
        percentage.append(vprct)

    winner = votes.index(max(votes))

with open(output_file,"w") as txtfile:
    output = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {row_count:}\n"
        f"----------------------------\n")
    print(output)
    txtfile.write(output)


    for k in range(0, candicount):
        output_candidate = f"{candidates_list[k]}: {percentage[k]:.3%} ({votes[k]:,})\n"
        print(output_candidate)
        txtfile.write(output_candidate)


    output = (
    f"----------------------------\n"
    f"Winner: {candidates_list[winner]}\n"
    f"----------------------------\n")

    print(output)
    txtfile.write(output)

