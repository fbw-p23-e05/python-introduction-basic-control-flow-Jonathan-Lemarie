
##  -----------  task 6  : which asks the user for a number and prints if a number is positive, odd and divisible by 7


number2 = int(input('enter number: '))

if number2 % 2 != 0 and number2 % 7 == 0 and number2 > 0:
    print(number2, 'is positive, odd and divisible by 7')