"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""

choco_size_m = 0
choco_size_n = 0
broken_pieces = 0

def main():
    global choco_size_m
    global choco_size_n
    global broken_pieces

    while True:
        choco_size_m = input('Введите число долек в шоколадке (длина) или "Q" для выхода:')
        if choco_size_m == 'Q':
            exit()
        status_code = 'm'
        check_input(status_code)

        choco_size_n = input('Введите число долек в шоколадке (ширина) или "Q" для выхода:')
        if choco_size_n == 'Q':
            exit()
        status_code = 'n'
        check_input(status_code)

        broken_pieces = input('Введите количество долек или "Q" для выхода:')
        if choco_size_n == 'Q':
            exit()
        status_code = 'b'
        check_input(status_code)

        print('СЛОМАТЬ, нельзя оставить!' if (broken_pieces % choco_size_m == 0 or  broken_pieces % choco_size_n == 0) else 'СЛОМАТЬ НЕЛЬЗЯ, оставить!')

def check_input(status_code):
    global choco_size_m
    global choco_size_n
    global broken_pieces

    while True:
        try:
            choco_size_m =int(choco_size_m)
            choco_size_n =int(choco_size_n)
            broken_pieces = int(broken_pieces)
            return choco_size_m, choco_size_n, broken_pieces
        except:
            print('Ошибка ввода!')
            if status_code == 'm':
                choco_size_m = input('Введите число долек в шоколадке (длина) или "Q" для выхода:')
            if status_code == 'n':
                choco_size_n = input('Введите число долек в шоколадке (ширина) или "Q" для выхода:')
            if status_code == 'b':
                broken_pieces = input('Введите количество долек или "Q" для выхода:')
            if choco_size_m == 'Q' or choco_size_n == 'Q' or broken_pieces == 'Q':
                exit()

main()

