
# Imp Dependencies
import os
import csv

# DeclVar
total_months = 0
net_amount = 0
month_count = []
monthly_change = []

biggest_increase = 0
biggest_increase_month = 0
biggest_decrease = 0
biggest_decrease_month = 0

# Set Path For File
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as budget_data:
    
    csvreader = csv.reader(budget_data, delimiter=',')
    
    # Read The Header Row First
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate Mmonths, profits/Loss
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    biggest_increase = int(row[1])
    biggest_increase_month = row [0]
    #Set rowvar
    for row in csvreader:

        # calc total number of months
        total_months += 1

        # calc Net P/L for whole period
        net_amount += int(row[1])

        # calc current to previous month diff
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # calc biggest increase
        if int(row[1]) > biggest_increase:
                biggest_increase = int(row[1])
                biggest_increase_month = row[0]
            
        # calc biggest decrease
        if int(row[1]) < biggest_decrease:
                biggest_decrease = int(row[1])
                biggest_decrease_month = row[0]  
        
    # calc  average & date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print the analysis
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {biggest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {biggest_decrease_month}, (${lowest})")

# File location
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data_revised.text')
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {biggest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {biggest_decrease_month}, (${lowest})\n")
