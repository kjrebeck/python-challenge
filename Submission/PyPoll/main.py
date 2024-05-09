#Referenced 3.2 08 Ins Read - reading in csvs and headers
#import mod to read csv file
import csv

#csv file path
csvpath= "PyPoll/Resources/election_data.csv"

#list to store each candidates vote
candidates={}
#starting number of votes
total_votes=0

#er3.2 Activities #08-Ins_ReadCSV 
#open csv file with utf-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row
    csv_header =next(csvreader)

    #read rows after header
    for row in csvreader:
        #each  row add 1 to total votes 
        total_votes= total_votes +1

        #extracts candidate from third column, store
        candidate = row[2]

        #check if candidate exists in dict of candidates
        #already in dict add 1 to count
        #Referenced 'Automate the boring stuff Ch 4     
        if candidate in candidates:
            candidates[candidate] +=1
        #not in dict, adds to list starts count at 1
        else:
            candidates[candidate]=1
        # #store analysis results"
        
        votingresults = (f"\nElection Results\n"
                   f"-------------------------\n"
                   #all ballots
                   f"Total Votes: {total_votes}\n"
                   f"-------------------------\n" +
                   #for each candidate return percentage of votes and count of votes
                   "\n".join([f"{candidate}: {round(((count/total_votes)*100),3)}% ({count})" 
                              for candidate, count in candidates.items()]) +
                   #return winner using max# 
                   f"\n-------------------------\nWinner: {max(candidates, key=candidates.get)}\n-------------------------")
        
    outputfile = "PyPoll/analysis/results.txt"
    with open (outputfile, mode='w', encoding='UTF-8') as output:
        output.write(votingresults)
        print(votingresults)


