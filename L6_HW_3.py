# https://github.com/Snakeinweb/L6_HW_3

a = int (input ())
b = int (input ())
while a > b:
    a = int (input ('������� ����� ������� ���� ������ ���������� ��������� �����: '))  
    b = int (input ('������� ����� ������ ���� ������� ���������������: '))
for i in range (a, b):
    if i%2 == 0:
        print (i, end=' ')
