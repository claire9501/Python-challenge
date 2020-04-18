#Read cvs.
import os
import csv

pybank_csv_path = os.path.dirname(__file__) + '/Resources/budget_data.csv'

with open(pybank_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)


    total_months = 0
    total_amount = 0
    previous = 0
    average_change = 0
    monthly_change = []
    date = []

    for row in csv_reader:
        #* The total number of months included in the dataset
        total_months += 1
        #* The net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])
        #* The average of the changes in "Profit/Losses" over the entire period
        average_change = average_change + (int(row[1]) - previous)
        monthly_change.append(int(row[1]) - previous)
        previous = int(row[1])
        date.append(str(row[0]))
    #* The greatest decrease in losses (date and amount) over the entire period
    #* The greatest increase in profits (date and amount) over the entire period
    monthly_change_max = max(monthly_change)
    monthly_change_min = min(monthly_change)
    max_increase_month = date[monthly_change.index(monthly_change_max)]
    max_decrease_month = date[monthly_change.index(monthly_change_min)]
        

    print("------------------------------------------------------------------------------")
    print("Finanical Analsis")
    print(f'Total Months:{total_months}')
    print(f'Total:" {total_amount}')
    print(f'Average Change:{average_change/(total_months)}')
    print(f'Greatest Increase in Profits {monthly_change_max}')
    print(f'Greatest Decrease in Profits {monthly_change_min}')
    print(f'Greatest Decrease Date is {max_decrease_month}')
    print(f'Greatest Increase Date is {max_increase_month}')
    print("------------------------------------------------------------------------------")
