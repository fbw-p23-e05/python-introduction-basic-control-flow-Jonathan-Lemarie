## -------- tASK 1 :


for _ in range(3):
    num = int(input('enter number: '))
    if num % 2 == 0:
        print('even number')
    else:
        print('odd number')


##  ---------- TASK 2 :

total_amount = 0

for _ in range(3):
    num = int(input('enter number: '))
    total_amount = total_amount + num


print('Sum of the numbers: ' , total_amount)


## --------   task 3


max_number = 0

for _ in range(5):
    num = int(input('enter number: '))
    if num > max_number:
        max_number = num

print('Maximum of the numbers: ', max_number)


## ----------  task 4

num = int(input('enter number: '))

for i in range(1, num+1):
     if num % i == 0:
         print(i)

## --------   task 5


number1 = int(input('enter number: '))

if number1 % 2 == 0 and number1 % 3 == 0:
    print(number1, 'is even and divisible by 3')



##  -----------  task 6


number2 = int(input('enter number: '))

if number2 % 2 != 0 and number2 % 7 == 0:
    print(number2, 'is positive, odd and divisible by 7')

