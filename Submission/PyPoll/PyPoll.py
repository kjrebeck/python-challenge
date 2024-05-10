#import mod to read csv file
import csv

#csv file path
csvpath= "Submission/Pypoll/Resources/election_data.csv"

#list to store each candidates vote
candidates={}
#starting number of votes
total_votes=0

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
        #already stored in list add 1 to count
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
                   #extracting values from lists within lists
                   #https://docs.python.org/3/library/stdtypes.html#
                   #https://docs.python.org/3/tutorial/datastructures.html#data-structures
                   "\n".join([f"{candidate}: {round(((count/total_votes)*100),3)}% ({count})"
                              for candidate, count in candidates.items()]) +
                              #candidate name (key), vote count (value) stored as tuple,
                   #return winner using max# loops through candidate list- retrieves the value associated with a given key (most votes)
                   f"\n-------------------------\nWinner: {max(candidates, key=candidates.get)}\n-------------------------")
        
    outputfile = "Submission/PyPoll/Analysis/electionresults.txt"
    with open (outputfile, mode='w', encoding='UTF-8') as output:
        output.write(votingresults)
        print(votingresults)


