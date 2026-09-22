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

with open("Report.txt", 'w') as output:
    output.write("Programmer: Iakimovich Sergey\n")
    output.write(input_lines[0]+'\n\n')
    output.write(f"Precipitation report for {input_lines[1]} during {input_lines[2]}\n")

month = list(calendar.month_abbr).index(input_lines[2].split(", ")[0][:3])
year = int(input_lines[2].split(", ")[1])
num_of_days = monthrange(year, month)[1]

data = {}
did_err_head_print = False
for line_num in range(3, len(input_lines)):
    line = input_lines[line_num]
    if not line:
        continue
    errors = ""
    day, inches = list(map(D, line.split()))
    if day > D(str(num_of_days)) or day < D(str(1)):
        errors += "Invalid "
    if day in data:
        errors += "Repeated "
    if errors:
        if not did_err_head_print:
            did_err_head_print = True
            with open("Report.txt", 'a') as output:
                output.write(f"\n{"Error":<9}{"Day":>8}{"Line":>11}\n")
        for error in errors.split():
            with open("Report.txt", 'a') as output:
                output.write(f"{error:<9}{day:>8}{line_num+1:>11}\n")
    if not errors:
        data[day] = inches

min_amount = None
max_amount = None
average_amount = None
with open("Report.txt", 'a') as output:
    output.write(f"\nDay Amount Graph\n")
for i in range(1, num_of_days+1):
    day = D(i)
    inch_in_day = None
    graph_len = 0
    if day in data:
        inch_in_day = data[day].quantize(D("0.01"), ROUND_HALF_UP)
        measure = D("0.25")
        graph_len = int(D(inch_in_day/measure).quantize(D('0'), ROUND_UP))
        if average_amount is not None:
            average_amount += inch_in_day
        if min_amount is None:
            min_amount = max_amount = average_amount = inch_in_day
        elif min_amount > inch_in_day:
            min_amount = inch_in_day
        if max_amount < inch_in_day:
            max_amount = inch_in_day
    graph = "*"*graph_len
    with open("Report.txt", 'a') as output:
        output.write(f"{day:>3}{"NA" if inch_in_day is None else inch_in_day:>7} {graph}\n")

if average_amount is not None:
    average_amount = D(average_amount/D(num_of_days)).quantize(D("0.01"))
else:
    average_amount = min_amount = max_amount = "NA"
with open("Report.txt", 'a') as output:
    output.write("\nMinimum     Maximum     Average\n")
    output.write(f"{min_amount:>7}{max_amount:>12}{average_amount:>12}\n")
