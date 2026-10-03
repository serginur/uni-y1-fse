from sys import argv

input_list = []
if len(argv) > 1:
    for i in range(1, len(argv)):
        input_list.append(argv[i])
else:
    print(f"!-- usage: python {argv[0]} text to shorten")
    exit(0)
