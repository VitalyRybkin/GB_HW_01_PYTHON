"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
"""

happy_ticket = ''

def main():
    print('ФЕДЕРАЛЬНАЯ ПРОГРАММА ПРОВЕРКИ СЧАТЛИВЫХ БИЛЕТОВ.')
    global happy_ticket
    while True:
        happy_ticket = input('Введите номер билета из 6 цифр или "Q" для выхода:')
        if happy_ticket == 'Q':
            exit()

        check_input()

        if len(str(happy_ticket)) != 6:
            print('Ошибка ввода!')
            continue

        first_sum = sum(map(int, str(str(happy_ticket)[0:3])))
        sec_sum = sum(map(int, str(str(happy_ticket)[3:])))

        print('Билет счастливый!' if first_sum == sec_sum else 'Билет несчастливый!')


def check_input():
    global happy_ticket
    try:
        happy_ticket = int(happy_ticket)
        return happy_ticket
    except:
        print('Введено неправильное число!')
        happy_ticket = input('Введите номер билета из 6 цифр или "Q" для выхода:')
        if happy_ticket == 'Q':
            exit()

main()

