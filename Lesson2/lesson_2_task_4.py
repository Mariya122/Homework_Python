fizz_buzz = range(55)
for num in fizz_buzz:
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz')
    elif (num % 3 == 0):
        print('Fizz')
    elif (num % 5 == 0):
        print('Buzz')
    else:
        print(num)
    
print(num)