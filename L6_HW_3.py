# https://github.com/Snakeinweb/L6_HW_3

a = int (input ())
b = int (input ())
while a > b:
    a = int (input ('Введите число меньшее либо равное следующему вводимому числу: '))  
    b = int (input ('Введите число равное либо большее препредъидущиму: '))
for i in range (a, b+1):
    if i%2 == 0:
        print (i, end=' ')
