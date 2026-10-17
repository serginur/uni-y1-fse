from sys import argv
from collections import Counter

def decode_seq(seq:str) -> str:
    if seq.isalpha():
        return seq

    found_digit = None
    decoded_token = ""
    for ch in seq:
        if found_digit:
            decoded_token += ch*found_digit
            found_digit = None
            continue
        if ch.isdigit():
            found_digit = int(ch)
            continue
        else:
            decoded_token += ch
    return decoded_token

seq_file_path = "a4_task_files/sequences.0.txt"
com_file_path = "a4_task_files/commands.0.txt"
if (len(argv) == 3):
    seq_file_path = argv[1]
    com_file_path = argv[2]

sequences: list[dict[str, str]] = []
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

commands: list[dict[str, str]] = []
try:
    with open(com_file_path) as com_file:
        for line in com_file.read().split('\n'):
            if line:
                tokens = line.split('\t')
                tokens_to_append = []
                for i in range(1, len(tokens)):
                    tokens_to_append.append(decode_seq(tokens[i]))
                if (len(tokens) > 2):
                    commands.append({"command": tokens[0],\
                                    "params": f"{tokens_to_append[0]}\t{tokens_to_append[1]}"})
                else:
                    commands.append({"command": tokens[0],\
                                    "params": tokens_to_append[1]})
except FileNotFoundError:
    print("Файл или директория отсутствует!")
    exit(0)

with open("genedata.txt", 'w') as out:
    out.write("Sergey Iakimovich\n")
    out.write("Genetic Searching\n")
    out.write(f"{"-"*80}\n")

operation_index = 0
for command in commands:
    operation_index += 1
    print(f"{operation_index:03d}\t{command["command"]}\t{command["params"]}")
    match command["command"]:
        case "search":
            print("organism\t\t\tprotein",end='')
            found = ""
            for seq in sequences:
                if command["params"] in seq["amino-acid"]:
                    found += f"\n{seq["entity"]}\t\t\t{seq["protein"]}"
            if found:
                print(found)
            else:
                print("\nNOT FOUND")

            print("-"*80)
        case "diff":
            print("amino-acids difference:")
            proteins = tuple(command["params"].split('\t'))
            compared = {protein: seq["amino-acid"]\
                            for protein in proteins for seq in sequences\
                                if seq["protein"] == protein}
            missing = [protein for protein in proteins if protein not in compared]
            if missing:
                print(f"MISSING: {", ".join(miss for miss in missing)}")
            else:
                acid1, acid2 = tuple(compared.values())
                diff = abs(len(acid1) - len(acid2))
                for i in range(min(len(acid1), len(acid2))):
                    diff += 1 if acid1[i] != acid2[i] else 0
                print(f"{diff}")
        case "mode":
            print("amino-acid occurs")
            max_repeat = None
            for seq in sequences:
                if seq["protein"] is command["params"]:
                    max_repeat = Counter(sorted(seq["amino-acid"])).most_common(1)[0]
            if max_repeat:
                print(f"{max_repeat[0]}\t\t{max_repeat[1]}")
            else:
                print(f"MISSING: {command["params"]}")
        case _:
            pass
    print("-"*80)
