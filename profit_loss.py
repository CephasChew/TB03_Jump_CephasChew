from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv
from posixpath import sep
import re

# def profitloss_function(forex):

#Creating empty list
empty_list=[]

# create file paths for Profits and Loss.csv and summary_report.txt
file_path=Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"

#to open the file
with file_path.open(mode='r', encoding= 'UTF-8', newline= '') as file:
    reader=csv.reader(file)
    #reading the csv file
    next(reader)
    #for... in loop to iterate over the list
    for line in reader:
        for info in line:
            #to append item at the end of the list
            empty_list.append(info)
# print(empty_list)

#creating a new list
new_list=[]
for info in empty_list:
    #for ... in loop to iterate over the list
    info = int(info)
    #change the numbers into integers with int()
    new_list.append(info)
# print(new_list)
#count the number of elements in the new list with len()
no=(len(new_list))
#creating a new list for the deficit
deficit_list=[]

for num in range (no):
    if num%5==4:
        #comparing values and setting condition
        deficit_list.append(new_list[num])
    # print(deficit_list)
    # print(len(deficit_list))
for i in range((len(deficit_list))-1):
    deficit_list[i] = deficit_list[i] - deficit_list[i+1]
deficit_list.pop()


positive_deficit_values=[]
deficit_days=[]
for values in deficit_list:
    if values>0:
        positive_deficit_values.append(values)
        index= deficit_list.index(values)
        new_list_index=((index+4)*2)
        deficit_days.append(new_list[new_list_index])

for i in range(len(deficit_days)):
    with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(f"\n[PROFIT DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]} ")