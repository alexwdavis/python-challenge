import pandas as pd

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
#maximum_month =
#minimum_month = 

average_change_print = "Average Change: " + "$" + str(average)
greatest_increase_print = "Greatest Increase in Profits: " + "$" + str(maximum)
greatest_decrease_print = "Greatest Decrease in Profits: " + "$" + str(minimum)
#for budget in budget_column:
#    if budget == "!":
#       budget_difference = (budget[2]) + (budget[3])
#        budget.next()
#        continue

#def budget_column(square):
#    output = []
#    for i in budget_column(2, 86):
#        total = 0

#        for row in square:
#            total += row[i]

#        output.append(total)
#    return output

print ("                  ")
print ("Financial Analysis")
print ("----------------------------")
print (month_count_print)
print (net_total_print)
print (average_change_print)
print (greatest_increase_print)
print (greatest_decrease_print)