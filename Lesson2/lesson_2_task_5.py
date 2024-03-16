month_to_season = input("Введите число месяца от 1 до 12")
month = int(month_to_season)

print(month)
feedback = ""
if (month == 12) or (month == 1) or (month == 2):
    feedback = ("Зима")

elif (month == 3) or (month == 4) or (month == 5):
    feedback = ("Весна")

elif (month == 6) or (month == 7) or (month == 8):
    feedback = ("Лето")

elif (month == 9) or (month == 10) or (month == 11):
    feedback = ("Осень")

else:
    feedback = ("Введите корректное число месяца")

print(feedback)

