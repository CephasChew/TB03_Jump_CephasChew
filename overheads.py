from pathlib import Path
import csv

empty=[]

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"

with overheads.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
                empty.append(line[1])
                
new=[]
for info in empty:
        info= float(info)
        new.append(info)

print(new)

def highest():
        largestvalue=-1

        for each in (new):
                if each > largestvalue:
                        largestvalue = each

        print("[HIGHEST OVERHEADS] Salary Expense:", largestvalue)
highest()
                