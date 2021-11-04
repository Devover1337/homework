# Задача номер 3 первого урока по изучению Python.

numb = int(input('Введите тестируемое число: '))

if numb >= 11 or numb <= 19:
    print(numb, 'процентов')

elif numb % 10 == 1:
    print(numb, 'процент')


elif numb % 10 == 5:
    print(numb, 'процентов')

elif numb % 10 == 6:
    print(numb, 'процентов')

elif numb % 10 == 7:
    print(numb, 'процентов')

elif numb % 10 == 8:
    print(numb, 'процентов')

elif numb % 10 == 9:
    print(numb, 'процентов')

elif numb % 10 == 0:
    print(numb, 'процентов')


else:
    print(numb, 'процента')
