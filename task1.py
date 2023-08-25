## -------- tASK 1 :  code which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.

for _ in range(3):    
    num = int(input('enter number: '))
    if num % 2 == 0:
        print('even number')
    else:
        print('odd number')