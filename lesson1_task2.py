#Залача номер 1 из первого урока по Python.


seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

sec = int(input("Введите ваше число: "))

day = sec // seconds_in_day
sec = sec - (day * seconds_in_day)

hour = sec // seconds_in_hour
sec = sec - (hour * seconds_in_hour)

min = sec // seconds_in_minute
sec = sec - (min * seconds_in_minute)

print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(
day, hour, min, sec))