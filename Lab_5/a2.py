from sys import argv
import re

text = None
if len(argv) > 2:
    print(f"!--usage: python {argv[0]} [\"the text\"]")
    exit(0)
if len(argv) > 1:
    text = argv[1]

if text is None:
    text = input("Введите текст:")

sentenses = re.split(r"(?<=[?!.])", text)

for _ in range(sentenses.count('')):
    sentenses.remove('')

for s in sentenses:
    print(s)

print(f"Предложений в тексте: {len(sentenses)}")

