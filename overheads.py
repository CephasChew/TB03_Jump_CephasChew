from pathlib import Path
import csv
from unicodedata import category

file_path = Path.cwd()/"CSV_reports"/"Overheads.py"
with file_path.open(mode="r",encoding='UTF-8',newline ="") as file:
        text = file.read()
for file in file_path("Overheads.csv"):
    emptylist=[]
    category = ["Salary expense","Interest expense,Marketing expense","Overflow expense-retail","Overflow expense-warehouse","Penalty expense","Depreciation expense","Maintenanec expense","Shipping expense","Huamn resource expense"]
    overheads = [24.18,2.25,5.59,20.28,3.88,0.11,7.66,16.72,7.94,0.3,11.09]
    





            



