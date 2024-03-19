add_x = int(input('Введите сумму вклада:'))
add_y = int(input('Ведите срок вклада в годах:'))

def bank (x, y):
    i = 1
    while i <= y:
        x += x / 10
        i += 1
    return x

print(bank(add_x, add_y))