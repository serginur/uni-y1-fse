""" Напишите программу, которая считывает данные из файла ChaseData.txt,
содержащего данные о начальных позициях и перемещениях игроков, определяет
расстояние между игроками, расстояние, пройденное игроками за всю игру, а
также исход игры – «Кот поймал мышь» или «Мышь сбежала от кота» """

from sys import argv

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

C = {"row": "?", "col": "?", "dis": 0}
M = {"row": "?", "col": "?", "dis": -1}
is_caught = False

for command in commands:
    if (command[0] == "P"):
        print(f"({C["row"]:>2},{C["col"]:>2}){" "*4}", end='')
        print(f"({M["row"]:>2},{M["col"]:>2}){" "*4}", end='')
        if (C["row"] == "?" or M["row"] == "?"):
            print()
        else:
            print(f"{(abs(C["row"] - M["row"])+abs(C["col"] - M["col"])):>8}")
    elif (command[0] == "C" or command[0] == "M"):
        player = M if command[0] == 'M' else C
        if (player["row"] == "?"):
            player["row"] = int(command[1])
            player["col"] = int(command[2])
        else:
            player["row"] += int(command[1])
            if (player["row"] < 1):
                player["row"] += lines_num
            if (player["row"] > lines_num):
                player["row"] -= lines_num
            player["col"] += int(command[2])
            if (player["col"] < 1):
                player["col"] += columns_num
            if (player["col"] > columns_num):
                player["col"] -= columns_num
        if (player["dis"] == -1):
            player["dis"] = 0 
        else:
            player["dis"] += abs(int(command[1])) + abs(int(command[2]))
        if (M["col"] == C["col"] and M["row"] == C["row"]):
            is_caught = True
            break

print("-"*(7+4+7+4+8)+'\n\n')
print("Distance   Mouse    Cat")
print(f"{' '*11}{M["dis"]:>5}{C["dis"]:>7}\n")

if (is_caught):
    print(f"Mouse caught at: ({M["row"]},{M["col"]})")
else:
    print("Mouse evaded cat")
