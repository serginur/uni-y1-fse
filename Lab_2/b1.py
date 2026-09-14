from sys import argv
import os

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
map_scale = float(lines[0].split()[1])
distance_inches = []
for i in range(1, len(lines)):
    if (lines[i]):
        distance_inches.append(float(lines[i]))

print("Sergey Iakimovich")
print("Simple Map Distance Computations\n")
print(f"Map Scale Factor:\t{map_scale:.2f} miles per inch\n")

print("      Map       Mileage")
print("      Measure   Distance")
print("="*80)
total = 0.0
for i in range(number_of_locations):
    print(f"#  {i+1}    {distance_inches[i]:.1f}       {distance_inches[i] * map_scale:.1f}")
    total += round(distance_inches[i] * map_scale, 1)
print("="*80)
print(f"Total distance:    {round(total,1)} miles")
