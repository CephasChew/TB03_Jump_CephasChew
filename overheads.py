from pathlib import Path
import csv,api

# create a function 'overhead_function' with 'forex' as its parameter(to be used in main.py)
def overhead_function():
        
        # create an empty list and assign it to a variable 'empty'
        empty=[]
        # create another empty list and assign it to a variable 'category'
        category=[]

        # create file paths for CSV_reports, Overheads.csv and summary_report.txt 
        file_path = Path.cwd()/"CSV_reports"
        overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"
        summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"

        # open overheads.csv file in read mode
        with overheads.open(mode="r", encoding = "UTF-8") as file:
                # read the csv file using .reader()
                reader = csv.reader(file)
                # returns the next item in this iteration
                next(reader)
                # use a for loop to append the different categories into the empty list 'category' and 
                # to append the respective values for each category into the empty list 'empty'
                for line in reader:
                        empty.append(line[1])
                        category.append(line[0])
        # create a new empty list 'new'  
        new=[]
        # using a for loop, use float() to change the string values in 'empty' into a float and append 
        # these values into the new empty list 'new'
        for values in empty:
                values=float(values)
                new.append(values)           

        # create a function highest() 
        def highest():
                largestvalue=-1

                # create a for loop using the data from the empty list 'new'
                for each in (new):
                        # when the variable is greater than the largestvalue(assigned -1), the largest 
                        # value will be replaced by the variable and will no longer be -1. use the .index()
                        # function to index the largest value in the empty list 'new' and assign it to 
                        # a variable 'index'
                        if each > largestvalue:
                                largestvalue = each
                                index=(new.index(largestvalue))
                # open summary_path.txt in append mode and use .write() to append the largest value and 
                # its respective category into the text file with the title [HIGHEST OVERHEADS]
                with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
                        file.write(f"\n[HIGHEST OVERHEADS] {category[index]} : {api.api_function()*largestvalue}")
        # call the function 
        highest()
        
# call the function
overhead_function()
                