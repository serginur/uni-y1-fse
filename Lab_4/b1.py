import calendar
from sys import argv
from calendar import monthrange
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_UP

file_path = "b1_task_files/Precip.txt"
if (len(argv) > 1):
    file_path = argv[1]

input_lines = []
try:
    with open(file_path, 'r') as file:
        for line in file.read().split('\n'):
            if line:
                input_lines.append(line)
except FileNotFoundError:
    print("Файл или директория отсутсвует!")
    exit(0)
except PermissionError:
    print("Недостаточно прав доступа!")
    exit(0)

print("Programmer: Iakimovich Sergey")
print(input_lines[0]+'\n')
print(f"Precipitation report for {input_lines[1]} during {input_lines[2]}\n")

month = list(calendar.month_abbr).index(input_lines[2].split(", ")[0][:3])
year = int(input_lines[2].split(", ")[1])
num_of_days = monthrange(year, month)[1]

print(f"{"Error":<8}{"Day":>8}{"Line":>7}")

data = {}
for line_num in range(3, len(input_lines)):
    line = input_lines[line_num]
    if not line:
        continue
    error = False
    day, inches = list(map(D, line.split()))
    if day > D(str(num_of_days)) or day < D(str(1)):
        print(f"{"Invalid":<8}{day:>8}{line_num:>7}")
        error = True
    if day in data:
        print(f"{"Repeated":<8}{day:>8}{line_num:>7}")
        error = True
    if not error:
        data[day] = inches

min_amount = None
max_amount = None
average_amount = None
print(f"\nDay Amount Graph")
for i in range(1, num_of_days+1):
    day = D(i)
    inch_in_day = None
    graph_len = 0
    if day in data:
        inch_in_day = data[day].quantize(D("0.01"), ROUND_HALF_UP)
        measure = D("0.25")
        graph_len = int(D(inch_in_day/measure).quantize(D('0'), ROUND_UP))
        if min_amount is None:
            min_amount = max_amount = average_amount = inch_in_day
        elif min_amount > inch_in_day:
            min_amount = inch_in_day
        if max_amount < inch_in_day:
            max_amount = inch_in_day
        average_amount += inch_in_day
    graph = "*"*graph_len
    print(f"{day:>3}{"NA" if inch_in_day is None else inch_in_day:>7} {graph}")

if average_amount is not None:
    average_amount = D(average_amount/D(len(data))).quantize(D("0.01"))
else:
    average_amount = min_amount = max_amount = "NA"
print("\nMinimum     Maximum     Average")
print(f"{min_amount:>7}{max_amount:>12}{average_amount:>12}")
