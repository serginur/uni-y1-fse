from sys import argv
from calendar import monthrange

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

data_list = []
for i in range(3, len(input_lines)):
    error = False
    line = input_lines[i]
    day, inches = list(map(int, line.split()))
    if day > num_of_days or day < 1:
        print(f"{"Invalid":<8}{day:>8}{i:>7}")
        error = True
    for data in data_list:
        if day in data:
            print(f"{"Repeated":<8}{day:>8}{i:>7}")
            error = True
            break
    if not error:
        data_list.append([day, inches])

