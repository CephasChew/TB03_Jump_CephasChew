from pathlib import Path
import csv

file_path = Path.cwd()/"CSV_reports"/"Overheads.py"

with file_path.open(mode="w",encoding='UTF-8',newline ="") as file:

    for file in file_path("Overheads.csv"):
        emptylist=[]
with file.open(mode="r", encoding = "UTF-8") as file:
    text = file.read()

    





            



