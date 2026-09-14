from sys import argv
import os

file_path = "b1_task_files/inmap0.dat"
if (len(argv) > 1):
    file_path = argv[1]

content = None
try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Файл или директория отсутсвует!")
    exit(0)
except PermissionError:
    print("Недостаточно прав доступа!")
    exit(0)

print("Sergey Iakimovich")
print("Simple Map Distance Computations\n")
print("Map Scale Factor:\t")
