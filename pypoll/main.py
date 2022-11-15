import os
import csv

csvpath =os.path.join('resource','election_data.csv')
with open(csvpath,'r')as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)
    print(csvheader)
    total_num_votes = 0

    for row in csvreader:
           total_num_votes = total_num_votes + 1

     



print("Election Results")
print("=========================================================")
print(f"Total Votes: {total_num_votes}")

    
with open('analysis/results.text','w') as File:
        File.write(f'Financial Analysis\n')
        File.write("======================================================\n")
        File.write(f"Total Votes: {total_num_votes}\n")


