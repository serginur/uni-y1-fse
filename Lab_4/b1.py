from sys import argv
from calendar import monthrange
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_UP

file_path = "b1_task_files/Precip.txt"
if (len(argv) > 1):
    file_path = argv[1]

input_lines = []
try:
    with open(file_path, 'r') as file:
        input_lines = file.read().split('\n')
except FileNotFoundError:
    print("Файл или директория отсутсвует!")
    exit(0)
except PermissionError:
    print("Недостаточно прав доступа!")
    exit(0)

print("Programmer: Iakimovich Sergey")
print(input_lines[0]+'\n')
print(f"Precipitation report for {input_lines[1]} during {input_lines[2]}\n")

month, year = list(map(int, input_lines[2].split(", ")))
num_of_days = monthrange(month, year)[1]

print(f"{"Error":<8}{"Day":>8}{"Line":>7}")

data = {}
for line_num in range(3, len(input_lines)+1):
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

print(f"\nDay Amount Graph")
for i in range(1, num_of_days+1):
    day = D(i)
    inch = None
    graph_len = 0
    if day in data:
        inch = data[day].quantize(D("0.01"), ROUND_HALF_UP)
        measure = D("0.25")
        graph_len = int(D(inch/measure).quantize(D('0'), ROUND_UP))
    graph = "*"*graph_len
    print(f"{day:3>}{inch if inch else "NA":>7}{graph}")


