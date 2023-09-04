# https://github.com/Snakeinweb/L6_HW_3

a = int (input ())
b = int (input ())
while a > b:
    a = int (input ('¬ведите число меньшее либо равное следующему вводимому числу: '))  
    b = int (input ('¬ведите число равное либо большее препредъидущиму: '))
for i in range (a, b):
    if i%2 == 0:
        print (i, end=' ')
