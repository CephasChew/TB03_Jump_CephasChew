from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv,re
from posixpath import sep


# def coh_function(forex):

#create empty list
empty_list=[]   
#creating file path
file_path=Path(r"C:/Jump_python/CSV_reports/Cash on Hand.csv")

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
# print to check that the correct contents are in empty_list
print(empty_list)

#creating another empty list
new_list=[]
#for...in loop to iterate over the list
for info in empty_list:
    #turn the numbers in the list into integers
    info = int(info)
    #to append item at the back of the list
    new_list.append(info)
# print new_list to check that the content in the list is correct
print(new_list)

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

#range to repeat the code for the values in the list, temporary variable i to store integer value of current postition in range
for i in range((len(deficit_list))-1):
    #creating formula to find the deficit
    deficit_list[i]=(deficit_list[i]-deficit_list[i+1])
deficit_list.pop()

#creating new list for +ve deficit values and days where deficit occured
positive_deficit_values=[]
deficit_days=[]
#for...in loop to iterate over the list
for values in deficit_list:
    #setting conditions
    if values>0:
        #appending an item to the end of the list
        positive_deficit_values.append(values)
        index= deficit_list.index(values)
        new_list_index=((index+1)*2)
        deficit_days.append(new_list[new_list_index])

#to iterate over the list to get the values needed
for i in range(len(deficit_days)):
    print(f"The deficit value is ${positive_deficit_values[i]} on day {deficit_days[i]}")

    # summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"
    # with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
    #     file.write()
    


