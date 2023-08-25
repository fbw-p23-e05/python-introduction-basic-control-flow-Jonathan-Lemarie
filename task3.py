## --------   task 3  : code which asks the user five times for a number and prints the maximum of those numbers.


max_number = 0

for _ in range(5):
    num = int(input('enter number: '))
    if num > max_number:
        max_number = num

print('Maximum of the numbers: ', max_number)
