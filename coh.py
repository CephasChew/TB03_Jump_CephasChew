from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv,re
from posixpath import sep


# def coh_function(forex):
#create empty list
empty_list=[]   
#creating file paths for Cash on Hand.csv and for summary_report.txt
file_path=Path(r"C:/Jump_python/CSV_reports/Cash on Hand.csv")
summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"
#to open the file
with file_path.open(mode='r', encoding= 'UTF-8', newline= '') as file:
    #to read the csv file
    reader=csv.reader(file)
    #to obtain next value as file is being iterated through
    next(reader)
    #for...in loop to iterate over the list
    for line in reader:
        for info in line:
            #to append item at the end of the list
            empty_list.append(info)
#creating another empty list
new_list=[]
#for...in loop to iterate over the list
for info in empty_list:
    #turn the numbers in the list into float
    info = float(info)
    #to append item at the back of the list
    new_list.append(info)
#count the items in the new_list
no=(len(new_list))
#creating new list for deficit
deficit_list=[]
#for...in loop to iterate over the list
for num in range (no):
    #comparing values and setting condition
    if num%2==1:
        #appending values from one list into another
        deficit_list.append(new_list[num])
#This is to handle the scenario where cash on hand is in ascending order
#when i use sorted.(), it will arrange the values in the list in ascending order
#Thus, if cash on hand is always higher than the previous day, it will be ascending
if deficit_list==sorted(deficit_list):
    print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
#range to repeat the code for the values in the list, temporary variable i to store integer value of current postition in range
for i in range((len(deficit_list))-1):
    #creating formula to find the deficit
    deficit_list[i]=(deficit_list[i]-deficit_list[i+1])
#I use pop to remove the last value. This is because the last value will not be subtracted with anything
deficit_list.pop()
print(deficit_list)
#2 list, one to find out the differnce in values, the other to find out the days
positive_deficit_values=[]
deficit_days=[]
#for loop to find out which of the difference is positive
for values in deficit_list:
    if values>0:
        #append the positive values into the empty list
        positive_deficit_values.append(values)
        #find out the index of th eempty value in the deficit list
        index= deficit_list.index(values)
        #new index to allocate the date in new_list
        new_list_index=((index+1)*2)
        #append the data into the deficit_list
        deficit_days.append(new_list[new_list_index])
#for loops to iterate over the number of days to get the values needed
for i in range(len(deficit_days)):
    #printing the final statement
    print(f"\n[CASH DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]}")
#to iterate over the list to get the values needed
# for i in range(len(deficit_days)):
#     with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
#         file.write(f"\n[CASH DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]}")



