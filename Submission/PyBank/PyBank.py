#import mod to read csv file
import csv

#starting number of months
total_months = 0
#starting total profit
total_profit = 0

#store change and month as tuple
change_data=[]

#csv file path
csvpath= "Submission/Pybank/Resources/budget_data.csv"
#open csv file with utf-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row
    csv_header =next(csvreader)

    #begin loop, evaluating data row by row
    for row in csvreader:
        #set first month 
        month=row[0]
        profit=int(row[1])
        #total months - add 1 each row
        total_months +=1

        #add months profit to total profit
        total_profit += profit

        #changes, current month profit - prior month profit, starting in first row
        #first row of data if total month is >1 
        #Reference Automate the Boring Stuff Chapter 4 
        if total_months > 1:
            change = profit- prev_month_profit
            change_data.append((month, change))
            #add month and changes to tuple
        #reset changes for following month
        #current months profit will become previous month
        prev_month_profit= profit

#list comprehension - values from lists in tuples
#https://docs.python.org/3/tutorial/datastructures.html#data-structures""
#iterate/unpack tuple - extracting change, discard month, store in changes
changes = [change for _, change in change_data]
#average change = sum of changes/ count of changes
mean_changes = sum(changes) / len(changes)
#round to 2 decimal places
mean_rounded = round(mean_changes, 2)
       
#locate max profit change in changes
max_change = max(changes)
#find max profit change in change {}, return with corresponding month
max_month = next(month for month, change in change_data if change == max_change)
#locate min profit change in changes
min_change = min(changes)
#find max profit change in change {}, return with corresponding month
min_month = next(month for month, change in change_data if change == min_change)
           

#store analysis results"

analysisresults= (f"Financial Analysis\n"
                                
                f"-----------------\n"
                #print total months to table
                f"Total Months: {total_months}\n"
                #print total profit to table $
                f"Total Profit: ${total_profit}\n"
                #print average profit change $
                f"Average Change: ${mean_rounded}\n"
                #print max change and month $
                f"Greatest Increase in Profits: {max_month} (${max_change})\n"
                #print min change and month $
                f"Greatest Decrease in Profits: {min_month} (${min_change})\n")
#print results to terminal
print(analysisresults)

#printing results to txt file
#file path
outputfile = "Submission/PyBank/Analysis/financialresults.txt"
with open (outputfile, mode='w', encoding='UTF-8') as output:
    output.write(analysisresults)

