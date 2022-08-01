from pathlib import Path
import csv
file_1 = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
file1 = open(Path.cwd()/"CSV_reports"/"Cash on Hand.csv")
writer = csv.writer(file1)

for file in file_1:
    f = open(file, "r")
    coh = f.read()

    

