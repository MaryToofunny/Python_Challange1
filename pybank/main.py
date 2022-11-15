import os
import csv
csvpath = os.path.join('Resource','budget_data.csv')
with open(csvpath, 'r') as csvfile:
        csvreader =csv.reader(csvfile,delimiter=",")
        csvheader = next(csvreader)
        print(csvheader)
        monthcounter=0
        amount=0
        change=[]
        profit=[]
        date=[]
    
#Counting Rows and making a list for date and profit
        for row in csvreader:
                monthcounter +=1
                amount+= int(row[1])
                date.append(row[0])
                profit.append(row[1])
 #creating a list for calculating change
for i in range (1,monthcounter):
        chng= int(profit[i])-int(profit[i-1])
        change.append(chng)
 # Calculating Max and Min of Profit/loss       
max_change= int(change.index(max(change)))
min_change= int(change.index(min(change)))

# calculating the Month
for k in range(len(date)):
         if (k== max_change +1):
                  max_month =date[k]
         elif (k== min_change +1):
                 min_month=date[k]


print ("Financial Analysis")
print("======================================================")
print(f"Total months: {monthcounter}")
print(f"The net total amount of Profit/lossess over the entire period $ {amount}")
print(f"Average Change : ${sum(change)/len(change):.2f}")
print(f"Greates Increase in Profits :{max_month} ${max(change)}")
print(f"Greates Decrease in Profits:{min_month} ${min(change)}")

 #creating text file
with open('analysis/results.text','w') as File:
        File.write(f'Financial Analysis\n')
        File.write("======================================================\n")
        File.write(f"Total months: {monthcounter}\n")
        File.write(f"The net total amount of Profit/lossess over the entire period $ {amount}\n")
        File.write(f"Average Change : ${sum(change)/len(change):.2f}\n")
        File.write(f"Greates Increase in Profits :{max_month} ${max(change)}\n")
        File.write(f"Greates Decrease in Profits:{min_month} ${min(change)}\n")




    
