""" Напишите программу, которая считывает данные из файла ChaseData.txt,
содержащего данные о начальных позициях и перемещениях игроков, определяет
расстояние между игроками, расстояние, пройденное игроками за всю игру, а
также исход игры – «Кот поймал мышь» или «Мышь сбежала от кота» """

from sys import argv
from decimal import Decimal, ROUND_HALF_UP

file_path = "b1_task_files/1.ChaseData.txt"
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

lines_num, columns_num = input_lines[0].split()
lines_num = int(lines_num)
columns_num = int(columns_num)

commands = []
for i in range(1, len(input_lines)):
    if input_lines[i]:
        commands.append(list(input_lines[i].split()))
