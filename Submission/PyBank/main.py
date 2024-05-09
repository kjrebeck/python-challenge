#Referenced 3.2 08 Ins Read - reading in csvs and headers
#import mod to read csv file
import csv

#csv file path
csvpath= "../Resources/budget_data.csv"

#starting number of months
total_months= 0
#starting total profit
total_profit = 0

#list to store change and month
change_data=[]

#open csv file with utf-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row
    csv_header =next(csvreader)

    #read rows after header
    for row in csvreader:
        #set first month 
        month=row[0]
        profit=int(row[1])
        #total months - add 1 each row
        total_months +=1

        #add months profit to total profit
        total_profit += profit

        #changes, current month profit - prior month profit, starting in first row
        #first row of data if total month is 1 
        #Reference Automate the Boring Stuff Chapter 4 
        if total_months > 1:
            change = profit- prev_month_profit
            change_data.append((month, change))
        #reset changes for following month
        #current months profit will become previous month
        prev_month_profit= profit
            
changes = [change for _, change in change_data]
mean_changes = sum(changes) / len(changes)
mean_rounded = round(mean_changes, 2)
        #average change = sum of changes/ count of changes
        #round to 2 decimal places
    

            #find max profit change with corresponding month
    #get max from changes{} and store 
    
#get index val for max change and store
#locate max profit change in list changes 
max_change = max(changes)
#find max profit change in change {}, return with corresponding month
max_month = next(month for month, change in change_data if change == max_change)
#locate min profit change in profit changes list
min_change = min(changes)
#find max profit change in change {}, return with corresponding month
min_month = next(month for month, change in change_data if change == min_change)
            #find min profit change with corresponding month

        #store analysis results"
        #source automatetheboringstuff chapter 16
        #https://automatetheboringstuff.com/2e/chapter16/
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
outputfile = "../PyBank/analysis/results.txt"
with open (outputfile, mode='w', encoding='UTF-8') as output:
    output.write(analysisresults)

