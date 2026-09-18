from sys import argv

file_path = "b2_task_files/1.WCData.txt"
if (len(argv) > 1):
    file_path = argv[1]

lines = []
try:
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
except FileNotFoundError:
    print("Файл или директория отсутсвует!")
    exit(0)
except PermissionError:
    print("Недостаточно прав доступа!")
    exit(0)

time = []
air_temp = []
wind_speed = []
for i in range(2, len(lines)):
    if (lines[i]):
        line_split = lines[i].split()
        time.append(line_split[0])
        air_temp.append(line_split[1])
        wind_speed.append(line_split[2])
