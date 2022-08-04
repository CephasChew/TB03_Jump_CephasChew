from pathlib import Path
import csv

# def overhead_function(forex):
        
empty=[]
category=[]

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"
summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"

#creates 2 empty list to store category and overheads into a list
with overheads.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
                empty.append(line[1])
                category.append(line[0])
new=[]
for values in empty:
        values=float(values)
        new.append(values)           

#group it by using the define function and through using loop to find the latest value
def highest():
        largestvalue=-1

        for each in (new):
                if each > largestvalue:
                        largestvalue = each
                        index=(new.index(largestvalue))
        with summary_path.open(mode="a", encoding="UTF-8", newline="\n") as file:
                file.write(f"[HIGHEST OVERHEADS] {category[index]} : {largestvalue}")
highest()
                