import os
import csv

total_months=0
total=0
last_pl=0
average_change=0
change_in_pl=0
total_change=0
ginc_profits=0
gdec_profits=0
prev_change_in_pl=0
ginc_profits_month=""
gdec_profits_month=""

csvpath=os.path.join("..", "Resources", "budget_data.csv")

with open (csvpath, newline="") as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    print("csv_header", csv_header)
    
    for row in csvreader:
        month=row[0]
        total_months=total_months+1
        total = total + int(row[1])
        
        if total_months >1:
            change_in_pl=int(row[1])-last_pl
            total_change+=change_in_pl
            average_change=total_change/(total_months-1)
        
        last_pl=int(row[1])

        if  change_in_pl>ginc_profits:
            ginc_profits=change_in_pl
            ginc_profits_month=month
        
        elif change_in_pl<gdec_profits:
             gdec_profits=change_in_pl
             gdec_profits_month=month
             
print ("Financial Analysis")
print ("-------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {ginc_profits_month} ($ {ginc_profits})')
print(f'Greatest Decrease in Profits: {gdec_profits_month} ($ {gdec_profits})')

output= open("budget_data_output.txt","w+")
output.write("Financial Analysis \n")
output.write("------------------------------------- \n")
output.write(f'Total Months: {total_months}' + "\n")
output.write(f'Total: ${total}'+ "\n")
output.write(f'Average Change: ${average_change}'+ "\n")
output.write(f'Greatest Increase in Profits: {ginc_profits_month} ($ {ginc_profits})'+ "\n")
output.write(f'Greatest Decrease in Profits: {gdec_profits_month} ($ {gdec_profits})'+ "\n")
output.close()