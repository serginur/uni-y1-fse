from sys import argv

text = None
if len(argv) > 2:
    print(f"!-- usage: python {argv[0]} [\"text\"]")
    exit(0)
if len(argv) > 1:
    text = argv[1]

if text is None:
    text = input("Введите аббревируемый текст:\n")

abbr = ""
for word in text.split():
    if len(word) >= 3:
        abbr += word[0].upper()

print(abbr)
