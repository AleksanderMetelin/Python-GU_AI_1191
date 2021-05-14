'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, uhr, geld_im_uhr, duppel_geld = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", uhr)
print("Ставка в час: ", geld_im_uhr)
print("Премия: ", duppel_geld)

print('Зарплата сотрудника: ', (float(uhr) * float(geld_im_uhr) + float(duppel_geld)))

'''

2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

my_list = []
new = input('Введите числа через пробел: ').split()
for i in new:
    my_list.append(int(i))

res_list = [number for i, number in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]

print(my_list)
print(res_list)

'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их 
следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
a = [i for i in my_list]
print([i for i in a if a.count(i) == 1])


'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce
print(f'Результат умножения всех элементов списка {reduce(lambda x, y: x * y, [y for y in range(100, 1001) if y % 2 == 0])}')

'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, 
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

#а)
from itertools import count

start = int(input('Введите начальное число: '))
finisch = int(input('Введите конечное число: '))

for i in count(start):
    if i > finisch:
        break
    else:
        print(i)

#b)
from itertools import cycle

start = input('Введите последовательность символов: ')

a = 0
for i in cycle(start):
    if a > 10:
        break
    print(i)
    a += 1

'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор.
    Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, 
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''


def fact_gen(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp

n = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for f in fact_gen(n):
    print(f)
