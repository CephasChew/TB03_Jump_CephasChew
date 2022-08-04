from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv,re
from pickle import EMPTY_LIST
from posixpath import sep

def profitloss_function(forex):

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
new_list=[]
#for loop to iterate over the list
for number in empty_list:
    #changing the numbers from string to float
    number=float(number)
    #appending the new float values into an empty list
    new_list.append(number)
#Creating a deficit list to only include the net profit for each day
deficit_list=[]
#Counting the number of values in the list
no=len(new_list)
#for loop to iterate over the list in the range of the number of values
for num in range (no):
    #Choosing the values
    if num%5==4:
        #appending the values into a deficit list
        deficit_list.append(new_list[num])
#This is to handle the scenario where cash on hand is in ascending order
#when i use sorted.(), it will arrange the values in the list in ascending order
#Thus, if cash on hand is always higher than the previous day, it will be ascending
if deficit_list==sorted(deficit_list):
    print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
#For loop to find out the difference in profit everyday
for i in range(len(deficit_list)-1):
    deficit_list[i] = deficit_list[i] - deficit_list[i+1]
#I use pop to remove the last value. This is because the last value will not be subtracted with anything
deficit_list.pop()  
#2 list, one to find the difference in values, the other to find out the days
positive_deficit_values=[]
deficit_days=[]
#for loop to find out which of the differnce is positive
for values in deficit_list:
    if values>0:
        #append the positive values into the empty list
        positive_deficit_values.append(values)
        #find out the index of the empty value in the deficit list
        index= deficit_list.index(values)
        #New index to allocate the date in the "new_list"
        new_list_index=((index+4)*2)
        #append the date into the defict_days
        deficit_days.append(new_list[new_list_index])
#for loop to iterate over the number of days
for i in range(len(deficit_days)):
    #printing the final statement
    print(f"[PROFIT DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]}")

# for i in range(len(deficit_days)):
#     with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
#         file.write(f"\n[PROFIT DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]} ")

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

    # if the items in deficit_list are sorted in ascending order, append '[CASH SURPLUS] CASH ON EACH DAY IS 
    # HIGHER THAN THE PREVIOUS DAY' into the text file, summary_path.txt
    if deficit_list==sorted(deficit_list):
        with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
                file.write(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

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

profitloss_function()
