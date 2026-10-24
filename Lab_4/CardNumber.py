import re

def IsValidNumber(cardNumber):
    return cardNumber.isdigit() and len(cardNumber) in [13, 15, 16]

# оригинальный алгоритм вместо сборной солянки
def getCheckSum(cardNumber):
    checkSum = 0
    start_index = 1 - len(cardNumber)%2
    for i in range(start_index, len(cardNumber), 2):
        product = int(cardNumber[i])*2
        checkSum += (product - 9) if (product > 9) else (product)
    return checkSum


def isValidCheckSum(checkSum):
    return checkSum % 10 == 0

def getCardType(string):
    # приоритет логических операторов: not > and > or
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid" # неправильный отступ


cardNumber = input("Enter Card Number: ")
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        print(getCardType(cardNumber))
    # при валидном, но неверном checksum ничего бы не произошло, поэтому:
    else:
        print("Invalid checksum")
else:
    print("Wrong Input. Try again...")
