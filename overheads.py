from atexit import register
from pathlib import Path
import csv
from pickle import EMPTY_LIST
from platform import java_ver
import re
from unicodedata import category


file_path = Path.cwd()/"CSV_reports"
file_path = Path.cwd()/"CSV_reports"/"Overheads.csv"


with file_path.open(mode="r",encoding='UTF-8',newline ="") as file:
        reader=csv.reader(file)
        text = file.read() 
        category = re.findall(pattern="[A-Z].+", string=text)
        overheads = (re.findall(pattern="[0-9].+", string=text))

        print(category[0])
