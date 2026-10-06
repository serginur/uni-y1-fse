from sys import argv
import re

text = None
if len(argv) > 2:
    print(f"!-- usage: python {argv[0]} [\"the text\"]")
    exit(0)
if len(argv) > 1:
    text = argv[1]

if text is None:
    text = input("Введите текст:\n")

sentences = []
for sentence in re.split(r"(?<=[?!.]) ", text):
    if sentence:
        sentences.append(sentence.strip())

for sent in sentences:
    print(sent.strip())

print(f"Предложений в тексте: {len(sentences)}")

