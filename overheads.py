from pathlib import Path
import csv

def overhead_function(forex):
        
        empty=[]
        category=[]

        file_path = Path.cwd()/"CSV_reports"
        overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"

<<<<<<< HEAD

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"

#creates 2 empty list to store category and overheads into a list
with overheads.open(mode="r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
                empty.append(line[1])
                category.append(line[0])
                

=======
        #creates 2 empty list to store category and overheads into a list
        with overheads.open(mode="r", encoding = "UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                        empty.append(line[1])
                        category.append(line[0])

        #create another empty list change it into float
        new=[]
        for info in empty:
                info= float(info)
                new.append(info)
>>>>>>> df22d8fbe1d27a56751bc67bd72f15c82cbe3697

        #group it by using the define function and through using loop to find the latest value
        def highest():
                largestvalue=-1

<<<<<<< HEAD
print(new)

#group it by using the define function and through using loop to find the latest value
def highest():
        largestvalue=-1

        for each in (new):
                if each > largestvalue:
                        largestvalue = each
                        
                        index=(new.index(largestvalue))

        print("[HIGHEST OVERHEADS]",category[index],":", largestvalue)
highest()
=======
                for each in (new):
                        if each > largestvalue:
                                largestvalue = each

                print("[HIGHEST OVERHEADS]",category[0],":", largestvalue)
        highest()
>>>>>>> df22d8fbe1d27a56751bc67bd72f15c82cbe3697
                