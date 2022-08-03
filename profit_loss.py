from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv
from posixpath import sep
import re

empty_list=[]
file_path=Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
#Current working directory for the folder


with file_path.open(mode='r', encoding= 'UTF-8', newline= '') as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
        for info in line:
            empty_list.append(info)
print(empty_list)


new_list=[]
for info in empty_list:
    info = int(info)
    new_list.append(info)
print(new_list)

no=(len(new_list))

deficit_list=[]

for num in range (no):
    if num%5==4:
        deficit_list.append(new_list[num])
print(deficit_list)
print(len(deficit_list))

for i in range(len(deficit_list)-1):
    deficit_list[i] = deficit_list[i] - deficit_list[i+1]
deficit_list=(deficit_list[0:(len(deficit_list)-1)])
print(deficit_list)


positive_deficit_values=[]
deficit_days=[]
for values in deficit_list:
    if values>0:
        positive_deficit_values.append(values)
        index= deficit_list.index(values)
        new_list_index=((index+4)*2)
        deficit_days.append(new_list[new_list_index])
print(positive_deficit_values)
print(deficit_days)

for i in range(len(deficit_days)):
    print(f"[PROFIT DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]} ")