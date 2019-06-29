import os

import csv

from statistics import mean

budget_data_path = os.path.join('/Users/gmendoza/Documents/GitHub/python-challenge/Pybank/main.py','budget_data.csv')

total_month = 0 
total_revenue = 0 
change_in_revenue_list = []
previous_revenue = 0 

percent_increase = [" " ,0]
percent_decrease = [" " ,0]
                

month_revenue_change =[]




with open('budget_data.csv',newline='') as csvfile:
    read =csv.DictReader(csvfile)
    
    for row in read:

        #Tracking Total Months and Revenue 

         total_month = total_month + 1
         total_revenue = total_revenue + int(row["Profit/Losses"])

         #Calculate the total revenue and changes 

         change_in_revenue = (int(row["Profit/Losses"]) - previous_revenue)
         previous_revenue = (int(row["Profit/Losses"]))
         change_in_revenue_list = change_in_revenue_list + [change_in_revenue]
         month_revenue_change = month_revenue_change + [row["Date"]]
        
     
        
        #calculate percent increase and decrease 
         
         if (change_in_revenue > percent_increase[1]):
            percent_increase[0] = row["Date"]
            percent_increase[1] = change_in_revenue
         
         if change_in_revenue < percent_decrease[1] : 
             percent_decrease[0] = row["Date"]
             percent_decrease[1] = change_in_revenue
             
       
#Change in revenue        

average_change = total_revenue/total_month

print("--- Finacial Analysis----\n")
print (f"Total Months: {total_month}\n")
print(f"Greatest Increase in Revenue: {percent_increase[0]} (${percent_increase[1]:,.2f})\n")
print (f"Greatest Decrease in Revenue: {percent_decrease[0]} (${percent_decrease[1]:,.2f})\n")
print (f"Average Change: (${average_change:,.2f})\n",)
print (f"Total Revenue: (${total_revenue:,.2f})\n")