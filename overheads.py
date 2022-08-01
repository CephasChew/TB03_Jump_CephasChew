from atexit import register
from pathlib import Path
import csv
from platform import java_ver
import re
from unicodedata import category

file_path = Path.cwd()/"CSV_reports"
overheads = Path.cwd()/"CSV_reports"/"Overheads.csv"
overheads.touch

with file_path.open(mode="w",encoding='UTF-8',newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(["category","overheads"])
        file.close()

for file in file_path("*Overheads*.csv"):
        emptylist = []
with file_path.open(mode="r",encoding='UTF-8',newline ="") as file:
        text = file.read()
        Category = (re.search(pattern="Block.+", string=text))
        overheads = (re.findall(pattern="[0-9].+", string=text))


category = "Salary expense","Interest expense,Marketing expense","Overflow expense-retail","Overflow expense-warehouse","Penalty expense","Depreciation expense","Maintenanec expense","Shipping expense","Huamn resource expense"

overheads = (re.findall(pattern="[0-9].+", string=text))
for i in range (1):
        emptylist(max(overheads))
        
print(emptylist)
        









