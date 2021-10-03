# avg temperature in TLV is between -5 and 40 degrees
avg_temp1 = int(input('input your temperature'))
i = 1
while i < 10:
    if avg_temp1 > 40:
        print ('Your data is invalid')
        break
    if avg_temp1 < -5:
        print ('Your data is invalid')
        break
    avg_temp2 = int(input('input your temperature'))
    avg_temp1 = avg_temp2
    i = i + 1

if i == 10:
    print('Your data is valid')
