import pandas as pd
from pathlib import Path

budget_data = pd.read_csv("Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv", encoding="ISO-8859-1", delimiter=",")

month_count = len(budget_data["Date"].value_counts())
month_count_print = "Total Months: " + str(month_count)
net_total = budget_data["Profit/Losses"].sum()
net_total_print = "Total: " + "$" + str(net_total)
average_change = budget_data["Profit/Losses"].mean()
budget_column = budget_data["Profit/Losses"]

budget_column_shifted_column = budget_column.shift(1)
budget_column_difference = budget_column - budget_column_shifted_column


average = budget_column_difference.mean()
maximum = budget_column_difference.max()
minimum = budget_column_difference.min()    

#max_increase_month = budget_column_difference.index(max(budget_column_difference)) + 1
#max_decrease_month = budget_column_difference.index(min(budget_column_difference)) + 1

average_change_print = "Average Change: " + "$" + str(average)
greatest_increase_print = "Greatest Increase in Profits: " + "$" + str(maximum)
greatest_decrease_print = "Greatest Decrease in Profits: " + "$" + str(minimum)



print ("                  ")
print ("Financial Analysis")
print ("----------------------------")
print (month_count_print)
print (net_total_print)
print (average_change_print)
print (greatest_increase_print)
print (greatest_decrease_print)

total_file = Path("Financial_Analysis_Summary.txt")

with open(total_file,"w",) as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(month_count_print)
    file.write("\n")
    file.write(net_total_print)
    file.write("\n")
    file.write(average_change_print)
    file.write("\n")
    file.write(greatest_increase_print)
    file.write("\n")
    file.write(greatest_decrease_print)
