import os
import csv
from itertools import count

input_file = os.path.join("PyBank/Resources/budget_data.csv")
output_file = os.path.join("PyBank/analysis/budget_analysis.txt")

total_months = 0
total_budget = 0
change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999]


with open (input_file) as csvfile:
   # lines = csvfile.readlines()


   reader = csv.reader(csvfile)

   header_row = next (reader)
   first_data_row = next (reader)
   previous_value = int(first_data_row[1])
   total_months +=1 
   total_budget += int(first_data_row[1])

   
   for line in reader:
       total_budget += int(line[1])
       current_value = int(line[1])
       change = current_value - previous_value
       change_list.append(change)
       previous_value = current_value
       
       
       total_months +=1   

       if change > greatest_increase[1]:
           greatest_increase[1] = change
           greatest_increase[0] = line[0]

       if change < greatest_decrease[1]:
           greatest_decrease[1] = change
           greatest_decrease[0] = line[0]

average_change = round(sum(change_list)/len(change_list),2)
max_change = change_list.index(max(change_list))
min_change = change_list.index(min(change_list))

output = (
    f"Financial Analysis\n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_budget}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: ${greatest_increase}\n"
    f"Greatest Decrease in Profits: ${greatest_decrease}\n"

) 

print(output)

with open(output_file,"w") as txt_out:
    txt_out.write(output)




    
        