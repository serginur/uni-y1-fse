from sys import argv

seq_file_path = "a4_task_files/sequences.0.txt"
com_file_path = "a4_task_files/commands.0.txt"
if (len(argv) == 3):
    seq_file_path = argv[1]
    com_file_path = argv[2]

sequences: list[dict] = []
try:
    with open(seq_file_path) as seq_file:
        for line in seq_file.read().split('\n'):
            if line:
                tokens = line.split('\t')
                sequences.append({  "protein": tokens[0],\
                                    "entity": tokens[1],\
                                    "amino-acid": tokens[2]})
except FileNotFoundError:
    print("Файл или директория отсутствует!")
    exit(0)

commands: list[dict] = []
try:
    with open(com_file_path) as com_file:
        for line in com_file.read().split('\n'):
            if line:
                tokens = line.split('\t')
                if (len(tokens) > 2):
                    commands.append({"command": tokens[0],\
                                    "params": f"{tokens[1]}\t{tokens[2]}"})
                else:
                    commands.append({"command": tokens[0],\
                                    "params": tokens[1]})
except FileNotFoundError:
    print("Файл или директория отсутствует!")
    exit(0)
