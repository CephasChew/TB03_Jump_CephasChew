from ast import pattern
from dataclasses import replace
from operator import index
from pathlib import Path
import csv
from posixpath import sep

# create a function coh_function with forex as its parameter to be used in main.py
def coh_function():

    #create empty list
    empty_list=[]   
    #creating file paths for Cash on Hand.csv and for summary_report.txt
    file_path=Path(r"C:/Jump_python/CSV_reports/Cash on Hand.csv")
    summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"

    # open file_path in read mode
    with file_path.open(mode='r', encoding= 'UTF-8', newline= '') as file:
        # read the csv file(file_path) using csv.reader
        reader=csv.reader(file)
        # returns the next item in the iteration
        next(reader)
        # use for loop to iterate over reader
        for line in reader:
            for info in line:
                #to append item at the end of the list
                empty_list.append(info)

    #creating another empty list
    new_list=[]
    #using for loop to iterate over the list
    for info in empty_list:
        #turn the numbers in the list into integers
        info = int(info)
        #to append item at the end of the list
        new_list.append(info)

    #count the number of items in the new_list
    no=(len(new_list))

    #creating new list for deficit
    deficit_list=[]
    #using for loop to iterate over the list
    for num in range (no):
        #comparing values and setting condition
        if num%2==1:
            #appending values from new_list into deficit_list when condition is met
            deficit_list.append(new_list[num])

    # if the items in deficit_list are sorted in ascending order, append '[CASH SURPLUS] CASH ON EACH DAY IS 
    # HIGHER THAN THE PREVIOUS DAY' into the text file, summary_path.txt
    if deficit_list==sorted(deficit_list):
        with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
                file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    #range to repeat the code for the values in the list, temporary variable i to store integer value of 
    # current postition in range
    for i in range((len(deficit_list))-1):
        #creating formula to find the deficit
        deficit_list[i]=(deficit_list[i]-deficit_list[i+1])
    # use .pop() to remove the last value
    deficit_list.pop()

    #creating new lists for positive deficit values and days where deficit occured
    positive_deficit_values=[]
    deficit_days=[]
    #use for loop to iterate over the list
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
        with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
            file.write(f"\n[CASH DEFICIT] DAY: {deficit_days[i]}, AMOUNT: SGD{positive_deficit_values[i]}")


coh_function()



