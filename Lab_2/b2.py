from sys import argv
from decimal import ROUND_HALF_UP, Decimal as D

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

print(f"Time{"WC temp":>12}{"WC Effect":>14}")
print("-"*30)

WC_temps = []
i = 0
while (i < len(time)):
    Twc = D(D("35.74")+D("0.6125")*D(air_temp[i]) + (D("0.4275")*D(air_temp[i]) - D("35.75"))*D(wind_speed[i])**D("0.16")).quantize(D("0.1"))
    WC_temps.append(Twc)
    WC_effect = D(Twc - D(air_temp[i])).quantize(D("0.1"))
    print(f"{time[i]}{Twc:>8}{WC_effect:>14}")
    i += 1
print("-"*30)

i = 0
print(f"The average adjusted tempterature, based on {len(time)} observations, was ", end='')
avg_temp = D("0.0")
while (i < len(WC_temps)):
    avg_temp = avg_temp + WC_temps[i]
    i += 1

print(D(avg_temp/len(WC_temps)).quantize(D("0.1")))
