'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
'''

surname = input('Введите вашу фамилию:')
age = int(input('Введите ваш возраст:'))
street = input('Введите название улицы:')
num = int(input('Введите номер дома:'))
print(F"Привет {surname}, поздравляю тебя с твоим {age}-м днем рождения, "
      F"я очень рад, что ты живешь рядом со мной, по адресу {street}{num}")

'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
в формате чч:мм:сс. Используйте форматирование строк.
'''

vvod_sek = int(input('Введите время в секундах'))
h = int(vvod_sek / 60) // 60
m = int(vvod_sek / 60) % 60
sek = int(vvod_sek % 60)
print(F'{h}:{m}:{sek}')

'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

ip = int(input('Введите число'))
print(ip + (ip * 11) + (ip * 111))

'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

i = int(input('Введите целое число:'))
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)

'''
5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

proceeds = int(input('Введите полученную выручку:'))
costs = int(input('Введите понесенные издержки'))
profit = proceeds - costs
if proceeds > costs:
    staff = int(input('Введите численность сотрудников фирмы'))
    profitability = int((profit / proceeds) * 100)
    staff_profit = profitability / staff
    print(F'Предприятие, по итогам работы получило прибыль в размере {profit} рублей. '
          F'Рентабельность предприятия составляет {profitability} %. '
          F'Прибыль на одного сотрудника состовляет {staff_profit} рублей')
else:
    print(F'Предприятие, по итогам работы понесло убыток, в размере {profit} рублей.')

'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

km_a = int(input('Введите количество киломметров которое спортсмен пробежал за первый день:'))
km_b = int(input('Введите количество киломметров которое спортсмен должен пробегать в день:'))
b = 1
while km_a < km_b:
    km_a += ((km_a / 100) * 10)
    b += 1
print(F' Спортсмен достигнет требуемого результата на {b} день.')
