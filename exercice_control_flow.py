## -------- tASK 1 :  code which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.

for _ in range(3):    
    num = int(input('enter number: '))
    if num % 2 == 0:
        print('even number')
    else:
        print('odd number')


##  ---------- TASK 2 :  code which asks the user three times for a number and prints the sum of those numbers.

total_amount = 0

for _ in range(3):
    num = int(input('enter number: '))
    total_amount = total_amount + num


print('Sum of the numbers: ' , total_amount)


## --------   task 3  : code which asks the user five times for a number and prints the maximum of those numbers.


max_number = 0

for _ in range(5):
    num = int(input('enter number: '))
    if num > max_number:
        max_number = num

print('Maximum of the numbers: ', max_number)


## ----------  task 4  : which prints all the divisors of a number. The number comes from the user's input.

num = int(input('enter number: '))

for i in range(1, num+1):
     if num % i == 0:
         print(i)

## --------   task 5 : which asks the user for a number and prints if it is even and divisible by 3.


number1 = int(input('enter number: '))

if number1 % 2 == 0 and number1 % 3 == 0:
    print(number1, 'is even and divisible by 3')



##  -----------  task 6  : which asks the user for a number and prints if a number is positive, odd and divisible by 7


number2 = int(input('enter number: '))

if number2 % 2 != 0 and number2 % 7 == 0 and number2 > 0:
    print(number2, 'is positive, odd and divisible by 7')

