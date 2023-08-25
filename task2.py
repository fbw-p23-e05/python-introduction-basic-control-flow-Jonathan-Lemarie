##  ---------- TASK 2 :  code which asks the user three times for a number and prints the sum of those numbers.

total_amount = 0

for _ in range(3):
    num = int(input('enter number: '))
    total_amount = total_amount + num


print('Sum of the numbers: ' , total_amount)