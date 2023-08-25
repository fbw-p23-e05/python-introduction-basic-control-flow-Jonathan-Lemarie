## ----------  task 4  : which prints all the divisors of a number. The number comes from the user's input.

num = int(input('enter number: '))

for i in range(1, num+1):
     if num % i == 0:
         print(i)
