# insert 10 positive numbers
i = 1
number1 = int(input('Insert an integer number'))
number2 = int(input('Insert an integer number'))
while i < 9:
    number3 = int(input('Insert an integer number'))
    sum_of_numbers = number2 + number1
    if sum_of_numbers == number3:
        print('The number you chose equals to the sum of all numbers', number3)
        break
    sum_of_numbers = sum_of_numbers+number3
    number2 = number1
    number3 = number2
    i = i+1
if i == 9:
    print('Not found')
