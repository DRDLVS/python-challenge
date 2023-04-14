import csv


with open ("PyBank/Resources/budget_data.csv",mode="r") as csvfile:
   # lines = csvfile.readlines()
   reader = csv.reader(csvfile)
   next (reader)
   for line in reader:
       print(line[0], line[1])
    