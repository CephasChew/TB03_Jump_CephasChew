from pathlib import Path
import csv
import re
from unicodedata import category


empty=[]

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"
overheads.touch()
overheads_list = [["Salary Expense",24.18], ["Interest Expense",2.25], ["Marketing Expense",5.59],["Rental Expense",20.28],["Overflow Expense - Retail",3.88],["Overflow Expense - Warehouse",0.11],["Penalty Expense",7.66],["Depreciation Expense",16.72],["Maintenance Expense",7.94],["Shipping Expense",0.3],["Human Resource Expense",11.09]]

with overheads.open(mode="w", encoding = "UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Overheads"])
        for sublist in overheads_list:
                writer.writerow(sublist)
file.close()


with overheads.open(mode="r", encoding = "UTF-8") as file:
        text = file.read()
        category = (re.findall(pattern="[A-Z].+", string=text))
        max=(category)
print(max)