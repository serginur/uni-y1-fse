seconds_passed = int(input("Введите число секунд, прошедшее с начала суток: "))

clock_hours = seconds_passed//(60**2)
clock_minutes = (seconds_passed - clock_hours * 60**2)//60
clock_seconds = seconds_passed - clock_hours * 60**2 - clock_minutes * 60
if clock_hours > 24:
    clock_hours -= (clock_hours//24)*24

print("{}:{:02}:{:02}".format(clock_hours, clock_minutes, clock_seconds))
