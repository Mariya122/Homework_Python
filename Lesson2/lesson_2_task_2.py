is_year_leap = int(input("Год"))
if (is_year_leap % 4 == 0):
    print("Год " + str(is_year_leap) + ": " + str(True))
else:
    print("Год " + str(is_year_leap) + ": " + str(False))
