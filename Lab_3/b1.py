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

print("Cat and Mouse\n")
print(f"{"Cat":^7}{" "*4}{"Mouse":^7}{" "*4}{"Distance":^8}")
print("-"*(7+4+7+4+8))

C = {"lin": "?", "col": "?"}
M = {"lin": "?", "col": "?"}
for command in commands:
    match command[0]:
        case "P":
            print(f"({C['lin']:>2},{C['col']:>2}){" "*4}", end='')
            print(f"({M['lin']:>2},{M['col']:>2}){" "*4}", end='')
            if (C["lin"] == "?" or M["lin"] == "?"):
                print()
            else:
                print(f"{abs(C["lin"] - M["lin"])+abs(C["col"] - M["col"]):^8}")
        case "C" | "M":
            player = M if command[0] == 'M' else C
            if (player["lin"] == "?"):
                player["lin"] = int(command[1])
                player["col"] = int(command[2])
            else:
                player["lin"] += int(command[1])
                if (player["lin"] < 1):
                    player["lin"] += lines_num
                if (player["lin"] > lines_num):
                    player["lin"] -= lines_num
                player["col"] += int(command[2])
                if (player["col"] < 1):
                    player["col"] += columns_num
                if (player["col"] > columns_num):
                    player["col"] -= columns_num

