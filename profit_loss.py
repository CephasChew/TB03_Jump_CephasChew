from pathlib import Path
import csv
file_path = Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
with open(file_path, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
day40 = data[1]
day41 = data[2]
day42 = data[3]
day43 = data[4]
day44 = data[5]
day45 = data[6]

np40 = int(day40[4])
np41 = int(day41[4])
np42 = int(day42[4])
np43 = int(day43[4])
np44 = int(day44[4])
np45 = int(day45[4])

if np41 < np40:
    print(f"[CASH DEFICIT] DAY: {day41[0]}, AMOUNT: SGD{abs(np41-np40)}")
elif np42 < np41:
    print(f"[CASH DEFICIT] DAY: {day42[0]}, AMOUNT: SGD{abs(np42-np41)}")
elif np43 < np42:
    print(f"[CASH DEFICIT] DAY: {day43[0]}, AMOUNT: SGD{abs(np43-np42)}")
elif np44 < np43:
    print(f"[CASH DEFICIT] DAY: {day44[0]}, AMOUNT: SGD{abs(np44-np43)}")
elif np45 < np44:
    print(f"[CASH DEFICIT] DAY: {day45[0]}, AMOUNT: SGD{abs(np45-np44)}")