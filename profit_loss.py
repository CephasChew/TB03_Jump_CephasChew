from pathlib import Path
import csv
empty_list = []
file_path = Path.cwd()/"CSV_reports"/"Profits and Loss.csv"
with file_path.open(mode='r',encoding='UTF-8',newline='') as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
        for value in line:
            empty_list.append(value)

new_list = []
for info in empty_list:
    info=int(info)
    new_list.append(info)

if new_list[4]>new_list[9]:
    net_profit = abs(new_list[9]-new_list[4])
    print(f'[PROFIT DEFICIT] DAY: {new_list[5]}, AMOUNT:SGD{net_profit}')
elif new_list[9]>new_list[14]:
    net_profit = abs(new_list[14]-new_list[9])
    print(f'[PROFIT DEFICIT] DAY: {new_list[10]}, AMOUNT:SGD{net_profit}')
elif new_list[14]>new_list[19]:
    net_profit = abs(new_list[19]-new_list[14])
    print(f'[PROFIT DEFICIT] DAY: {new_list[15]}, AMOUNT:SGD{net_profit}')
elif new_list[19]>new_list[24]:
    net_profit = abs(new_list[24]-new_list[19])
    print(f'[PROFIT DEFICIT] DAY: {new_list[20]}, AMOUNT:SGD{net_profit}')
elif new_list[24]>new_list[29]:
    net_profit = abs(new_list[29]-new_list[24])
    print(f'[PROFIT DEFICIT] DAY: {new_list[25]}, AMOUNT:SGD{net_profit}')
else:
    print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")