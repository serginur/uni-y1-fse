from re import L
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
                command = tokens[0]
                match command:
                    case "diff":
                        params = f"{tokens[1]}|{tokens[2]}"
                    case "search":
                        params = decode_seq(tokens[1])
                    case _:
                        params = tokens[1]
                commands.append({"command": command, "params": params})
except FileNotFoundError:
    print("Файл или директория отсутствует!")
    exit(0)

# with open("genedata.txt", 'w') as out:
#     out.write("Sergey Iakimovich\n")
#     out.write("Genetic Searching\n")
#     out.write(f"{"-"*80}\n")

print("Sergey Iakimovich\n")
print("Genetic Searching\n")
print(f"{"-"*80}\n")

operation_index = 0
for command_dict in commands:
    command, params = command_dict.values()
    operation_index += 1
    print(f"{operation_index:03d}   {command}   {"   ".join(params.split('|'))}")
    match command:
        case "search":
            print(f"{"organism":<25}protein",end='')
            found = ""
            for sequence in sequences:
                protein, entity, amino_acid = sequence.values()
                if params in amino_acid:
                    found += f"\n{entity:<25}{protein}"
            if found:
                print(found)
            else:
                print("\nNOT FOUND")

        case "diff":
            print("amino-acids difference:")
            proteins = tuple(params.split('|'))
            compared = {}
            for sequence in sequences:
                protein, _, amino_acid = sequence.values()
                for comp_protein in proteins:
                    if comp_protein == protein:
                        compared[comp_protein] = amino_acid
            missing = [protein\
                        for protein in proteins if protein not in compared]
            if missing:
                print(f"MISSING: {", ".join(miss for miss in missing)}")
            else:
                if (len(compared) == 1):
                    print(0)
                else:
                    acid1, acid2 = tuple(compared.values())
                    diff = abs(len(acid1) - len(acid2))
                    for i in range(min(len(acid1), len(acid2))):
                        diff += 1 if acid1[i] != acid2[i] else 0
                    print(f"{diff}")
        case "mode":
            print("amino-acid occurs")
            max_repeat = None
            for sequence in sequences:
                protein, _, amino_acid = sequence.values()
                if protein == params:
                    max_repeat = Counter(sorted(amino_acid)).most_common(1)[0]
            if max_repeat:
                print(f"{max_repeat[0]:<11}{max_repeat[1]}")
            else:
                print(f"MISSING: {params}")
        case _:
            pass
    print("-"*80)
