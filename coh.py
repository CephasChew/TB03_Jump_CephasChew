from ast import pattern
from dataclasses import replace
from pathlib import Path
import csv
from posixpath import sep
import re

empty_list=[]
file_path=Path(r"C:/Jump_python/CSV_reports/Cash on Hand.csv")


with file_path.open(mode='r', encoding= 'UTF-8', newline= '') as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
       print(line)
       for value in line:
        empty_list.append(value)
print(empty_list)
        

new_list=[]
for info in empty_list:
    info=int(info)
    new_list.append(info)
print(new_list)

if new_list[1] > new_list[3]:
    deficit_amount= new_list[1]-new_list[3]
    print (f"Day:{new_list[2]}, Deficit amount:{deficit_amount}")   
if new_list[3] > new_list[5]:
    deficit_amount= new_list[3]-new_list[5]
    print (f"Day:{new_list[4]}, Deficit amount:{deficit_amount}")   
if new_list[5] > new_list[7]:
    deficit_amount= new_list[5]-new_list[7]
    print (f"Day:{new_list[6]}, Deficit amount:{deficit_amount}")   
if new_list[7] > new_list[9]:
    deficit_amount= new_list[7]-new_list[9]
    print (f"Day:{new_list[8]}, Deficit amount:{deficit_amount}")   
if new_list[9] > new_list[11]:
    deficit_amount= new_list[9]-new_list[11]
    print (f"Day:{new_list[10]}, Deficit amount:{deficit_amount}")

