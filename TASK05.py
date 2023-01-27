"""
Задача 2: - HARD необязательная, идет за 3 обязательных Найдите сумму цифр любого вещественного или целого числа.
Можно использовать decimal. Через строку решать нельзя.
"""

from decimal import Decimal

num = ''

def main():
    global num
    while True:
        num = input('Введите число или "Q", чтобы завершить программу: ')
        if num == "Q":
            exit()

        check_input()

        num_tail = num % 1
        while num_tail != 0:
            num = num * 10
            num_tail = num % 1

        num = int(num)

        num_sum = 0
        while num != 0:
            num_sum += num % 10
            num = int(num / 10)

        print(num_sum)
def check_input():
    global num
    while True:
        try:
            if num.isdigit():
                num = int(num)
                return num
            else:
                num = Decimal(num)
                return  num
        except:
            print('Ошибка ввода!')
            num = input('Введите новое число или "Q" для выхода: ')
            if num == "Q":
                exit()

main()