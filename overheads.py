from pathlib import Path
import csv


empty=[]
category=[]

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"

#creates 2 empty list to store category and overheads into a list
with overheads.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
                empty.append(line[1])
                category.append(line[0])

#create another empty list change it into float
new=[]
for info in empty:
        info= float(info)
        new.append(info)

#group it by using the define function and through using loop to find the latest value
def highest():
        largestvalue=-1

        for each in (new):
                if each > largestvalue:
                        largestvalue = each

        print("[HIGHEST OVERHEADS]",category[0],":", largestvalue)
highest()
                