# input numbers until number <= 0
max_number = 0
while True:
    number = int (input('input a number'))
    if number > max_number:
        max_number = number
    if number <= 0:
        break
print ('maximun number is ', max_number )
