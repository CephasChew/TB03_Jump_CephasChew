from ast import Num
from pathlib import Path
import csv
empty_list = []
file_path = Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
with file_path.open(mode='r',encoding='UTF-8',newline='') as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
        print(line)
        for value in line:
            empty_list.append(int(value))
print(empty_list)

1
if empty_list[4]>empty_list[9]:
    net_profit = abs(empty_list[9]-empty_list[4])
    print(f'[PROFIT DEFICIT] DAY: {empty_list[5]}, AMOUNT:SGD{net_profit}')
elif empty_list[9]>empty_list[14]:
    net_profit = abs(empty_list[14]-empty_list[9])
    print(f'[PROFIT DEFICIT] DAY: {empty_list[10]}, AMOUNT:SGD{net_profit}')
elif empty_list[14]>empty_list[19]:
    net_profit = abs(empty_list[19]-empty_list[14])
    print(f'[PROFIT DEFICIT] DAY: {empty_list[15]}, AMOUNT:SGD{net_profit}')
elif empty_list[19]>empty_list[24]:
    net_profit = abs(empty_list[24]-empty_list[19])
    print(f'[PROFIT DEFICIT] DAY: {empty_list[20]}, AMOUNT:SGD{net_profit}')
elif empty_list[24]>empty_list[29]:
    net_profit = abs(empty_list[29]-empty_list[24])
    print(f'[PROFIT DEFICIT] DAY: {empty_list[25]}, AMOUNT:SGD{net_profit}')
else:
    print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")