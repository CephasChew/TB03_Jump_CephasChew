from pathlib import Path
import csv
empty_list = []
file_path = Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
with file_path.open(mode='r',encoding='UTF-8',newline='') as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
        print(line)
#         for value in line:
#             empty_list.append(int(value))
# print(empty_list)