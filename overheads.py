from atexit import register
from pathlib import Path
import csv
from platform import java_ver
import re
from unicodedata import category

emptylist=[]

file_path = Path.cwd()/"CSV_reports"/"Overheads.csv"

with file_path.open(mode="r",encoding='UTF-8',newline ="") as file:
        text = file.read()
category = "Salary expense","Interest expense,Marketing expense","Overflow expense-retail","Overflow expense-warehouse","Penalty expense","Depreciation expense","Maintenanec expense","Shipping expense","Huamn resource expense"
overheads = (re.findall(pattern="[0-9].+", string=text))
for i in range (1):
        emptylist.append(category)
        emptylist.extend(overheads)
print(emptylist)
        









