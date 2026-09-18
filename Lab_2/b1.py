from sys import argv
from decimal import Decimal, ROUND_HALF_UP

file_path = "b1_task_files/inmap0.dat"
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

number_of_locations = int(lines[0].split()[0])
map_scale = Decimal(lines[0].split()[1]).quantize(Decimal("0.01"), ROUND_HALF_UP)
distance_inches = []
for i in range(1, len(lines)):
    if (lines[i]):
        distance_inches.append(Decimal(lines[i]).quantize(Decimal("0.1"), ROUND_HALF_UP))

print("Sergey Iakimovich")
print("Simple Map Distance Computations\n")
print(f"Map Scale Factor:\t{map_scale} miles per inch\n")

print("      Map\tMileage")
print("      Measure\tDistance")
print("="*80)
total = Decimal('0.0')
for i in range(number_of_locations):
    distance_inches_i = distance_inches[i]
    distance_miles_i = Decimal(distance_inches[i] * map_scale).quantize(Decimal('0.1'), ROUND_HALF_UP)
    spaces_to_print = 7 - len(str(distance_inches_i))
    print(f"#  {i+1}{' '*spaces_to_print}{distance_inches_i}\t  {distance_miles_i}")
    total += distance_miles_i
print("="*80)
print(f"Total distance:    {total} miles")
