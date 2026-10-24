import re
from sys import argv

def is_valid_number(card_number: str)->bool:
    return card_number.isdigit() and len(card_number) in [13, 15, 16]

def get_check_sum(card_number: str)->int:
    check_sum = 0
    start_index = 1 - len(card_number)%2
    for i in range(start_index, len(card_number), 2):
        product = card_number[i]*2
        check_sum += (product - 9) if product > 9 else product
    return check_sum

def is_valid_check_sum(check_sum: str)->bool:
    return not check_sum%10

def get_card_type(card_number: str)->str:
    starts = card_number[:2]
    length = len(card_number)
    return "American Express" if length == 15 and re.match(r"3[4,7]", starts)\
      else "Master Card" if length == 16 and re.match(r"5[1-5]", starts)\
      else "Visa" if length in [13, 16] and starts[0] == '4'\
      else "Номер не принадлежит ни к одной из известных платежных систем."


if __name__ == "__main__":
    card_number = ""
    if len(argv) == 2:
        card_number = argv[1]
    elif len(argv) > 2:
        print(f"!-- usage: python {argv[0]} [card_number]")
        exit(0)

    if not card_number:
        card_number = input("Введите номер карты: ")

    if is_valid_number(card_number):
        if is_valid_check_sum(get_check_sum(card_number)):
            print(get_card_type(card_number))
        else:
            print("Контрольная сумма номера невалидна")
    else:
        print("Ввод должен состоять из 13, 15 или 16 цифр!")
