from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv
from posixpath import sep
import re
#Creating empty list
empty_list=[]
file_path=Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
#Current working directory for the folder

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
print(empty_list)

#creating a new list
new_list=[]
for info in empty_list:
    #for ... in loop to iterate over the list
    info = int(info)
    #change the numbers into integers with int()
    new_list.append(info)
print(new_list)
#count the number of elements in the new list with len()
no=(len(new_list))
#creating a new list for the deficit
deficit_list=[]

for num in range (no):
    if num%5==4:
        #comparing values and setting condition
        deficit_list.append(new_list[num])
print(deficit_list)
print(len(deficit_list))

for i in range(len(deficit_list)-1):
    deficit_list[i] = deficit_list[i] - deficit_list[i+1]
deficit_list=(deficit_list[0:(len(deficit_list)-1)])
print(deficit_list)

#creating new lists for positive deficit values and deficit days
positive_deficit_values=[]
deficit_days=[]
for values in deficit_list:
    #for ... in loop to iterate over the list
    if values>0:
        positive_deficit_values.append(values)
        #appending the values to the end of the list
        index= deficit_list.index(values)
        new_list_index=((index+4)*2)
        deficit_days.append(new_list[new_list_index])
print(positive_deficit_values)
print(deficit_days)

for i in range(len(deficit_days)):
    print(f"[PROFIT DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]} ")
    

