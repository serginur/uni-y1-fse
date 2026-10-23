try:
    packets = input("Введите последовательность успешно доставленных и потерянных пакетов: ")
    while not all(char in '01' for char in packets) or len(packets) < 5:
        print("Неверный ввод.\nИспользуйте только символы '0' и '1' и длину строки больше 5 символов!")
        packets = input("Введите последовательность: ")
except (KeyboardInterrupt, EOFError):
    exit(0)

total_packets_amount = len(packets)
lost_amount = packets.count('0')

longest_lost_seq = 0
for lost_seq in packets.split('1'):
    if lost_seq and len(lost_seq) > longest_lost_seq:
        longest_lost_seq = len(lost_seq)

lost_percentage = (lost_amount/total_packets_amount)*100
net_quality = "отличное качество" if lost_percentage <= 1 else\
              "хорошее качество" if lost_percentage <= 5 else \
              "удовлетворительное качество" if lost_percentage <= 10 else\
              "плохое качество" if lost_percentage <= 20 else\
              "критическое состояние сети"

print(f"Общее количество пакетов: {total_packets_amount}")
print(f"Количество потерянных пакетов: {lost_amount}")
print(f"Длина самой длинной последовательности потерянных пакетов: {longest_lost_seq}")
print(f"Процент потерь: {lost_percentage}")
print(f"Качество связи: {net_quality}")
