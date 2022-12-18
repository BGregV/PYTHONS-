# Лекция 1

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
# print(f)
# print(not 1 in f)


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

# Лекция 2


# Хренение данных
# Передача данных в клиент-серверных проектах
# Хронение конфигов
# Логирование действий

# Связать файловую переменную с файлом, определив модификатор работ:
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - отклытие для записи данных
# w+, r+


# colors = ['red', 'geen', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителя не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()


# второе решение для создания и записи в файле
# with open('file.txt', 'w') as data:
#     data.write('LINE 12\n')
#     data.write('LINE 13\n')


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# импорт данных
# import sem.py as s
# print(s.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string('4'))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)


# Кортежи это неизменяемый список
# Кортеж может быть и из одного числа, то необходимо после числа ставить ","

# a = (3, 4)
# print(a[0])

# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

# distionary = {}
# distionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(distionary)
# print(distionary['left'])

# for k in distionary.keys():
#     print(k)
# for k in distionary.values():
#     print(k)
# for v in distionary:
#     print(v)



# Множества

# colors = {'red', 'geen', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)


# a = {1, 2, 3, 4, 5}
# b = {2, 8, 13, 5, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a \
#     .union(b) \
#     .difference(a.difference(b))
# print(q)


# Списки
# list = [1, 2, 3, 4, 5]
# list2 = list

# for e in list:
#     print(e)
# print()

# for e in list2:
#     print(e)


# list[0] = 123
# for e in list:
#     print(e)
# print()

# for e in list2:
#     print(e)

# list = [1, 2, 3, 4, 5]
# print(len(list))
# print(list.pop())
# print(list.pop())
# print(list.pop())
# print(list.pop())

# print(list.pop(2))
# print(list)

# print(list.insert(2, 11))
# print(list)
