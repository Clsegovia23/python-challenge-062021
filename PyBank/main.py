import os
import csv
#import math

#set path for file
#csv_reader = csv.DictReader(open('Resources/budget_data.csv'))
csvpath = os.path.join("Resources","budget_data.csv")

 #set up variables
count = 0
months = 0
average = 0
total = 0
current = 0
total_chg = 0
great_inc_profit = 0
great_decr_losses = 0
profit_inc_dates = ""
loss_decr_dates = ""


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period    
    
 #setup how to read data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(csvreader)
    count = 0
    total = 0
#The total number of months included in the dataset
    for row in csvreader:
        total += float(row[1])
        count += 1
        current = float(row[1])
        
   #The net total amount of "Profit/Losses" over the entire period 
    if(current >= 0): 
        if(current > great_inc_profit):
            great_inc_profit = current
            profit_inc_dates = str(row[0])
        elif(current < 0):
            if(current < great_decr_losses):
                great_decr_losses = current
                loss_decr_dates = str(row[0])
average = total / count
      
print(count, total) 

#with open(output_file, 'w') as csvfile:
 #   csvfile.write("Financial Analysis: ")
    
# printing summary:
#print("Total Months: " + str(row[0]))
#print("Total: " + float(row[1]))
#print("Average Change: " + avg... float(row[1])
#print("Greatest Increase in Profits: " + date... str(row[0] + float(row[1]))
#print("Greatest Decrease in Profits: " + date... str(row[0] + float(row[1]))