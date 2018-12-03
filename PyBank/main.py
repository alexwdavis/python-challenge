import pandas as pd

budget_data = pd.read_csv("Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv", encoding="ISO-8859-1")
month_count = len(budget_data["Date"].value_counts())
month_count_print = "Total Months: " + str(month_count)
net_total = budget_data["Profit/Losses"].sum()
net_total_print = "Total: " + "$" + str(net_total)
print ("                  ")
print ("Financial Analysis")
print ("----------------------------")
print (month_count_print)
print (net_total_print)
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")