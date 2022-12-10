# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(value)
# s = 'hello world'
# print(s)# вывод строки
# print(a, '-',b, '-', s)
# print(f'{a} - {b} - {s}')
# print ('{1} - {2} - {0}'.format(a, b, s))

# list = [1,2,3]
# print(list)

# print('Введите a');
# a =int(input())
# print('Введите b');
# b = int(input())
# print (a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')5
# print('Введите a');
# a =float(input())
# print('Введите b');
# b = float(input())
# print (a, ' + ', b, ' = ', a+b)
# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет в операциях
# **, *, /, //, %, +, -
# round - команда для ограничения знаков после запятой
# a = 2
# b = 8
# с= a-b
# print(с)
# Сокращенные операции
# a = 3
# a += 5
# print(a)

#Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &,|,^
# is, is not, in, not in
# gen

# func = 1
# T = 4
# x = 123
# print(func<T>x)

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)


# is_odd = f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Гриша':
#     print('Ура, это Гриша!')
# elif username == 'Марина':
#     print('Мы тебя ждали Марина)')
# elif username == 'Вася':
#     print('Вася привет!')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющая конструкция
# for

# r = range(10)
# for i in r:
#     print(i)
# for i in range(1, 10, 2):
#     print(i)

# Строки

# text = 'съешь еще этих мягких фрацузских булок'


# print(len(text))                 # 39
# print('еще' in text)             # True
# print(text.isdigit())            # False
# print(text.islower())            # True
# print(text.replace('еще','ещё')) #

# for c in text:
#     print(c)

# text = 'съешь еще этих мягких французских булок'
# print(text[0])
# print(text[1])
# # print(text[len(text)])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[2:5])
# print(text[len(text)-2])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# number = list(ran)
# print(numbers)
# print(type(number))

# numbers[0] = 10
# print(f'{len(number)}')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(number)

# Функции

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))