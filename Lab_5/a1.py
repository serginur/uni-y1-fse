from email.policy import default
from sys import argv

input_string = ""
if len(argv) > 1:
    for i in range(1, len(argv)):
        input_string += argv[i]
else:
    print(f"!-- usage: python {argv[0]} text to shorten")
    exit(0)

if '(' in input_string or ')' in input_string:
    count_brackets = [0, 0]
    for char in input_string:
        if char == '(':
            count_brackets[0] += 1
        elif char == ')':
            count_brackets[1] += 1
    if count_brackets[0] != count_brackets[1]:
        print(f"Количество открывающих ({count_brackets[0]}) и закрывающих ({count_brackets[1]}) скобок не равно!")
        exit(0)
    for i in range(count_brackets[0]):
        start = input_string.find('(')
        end = input_string.find(')')
        input_string = input_string.replace(input_string[start:end+1], '')
    output = input_string.split()
    out_string = output[0]
    output.remove(out_string)
    for token in output:
        match token:
            case '.' | ',' | ':' | ';':
                out_string += token
                break
            case _:
                out_string += ' ' + token
    print(out_string)
else:
    print("Скобки отсутствуют!")
    exit(0)
