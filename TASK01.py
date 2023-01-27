"""
Задача 2: Найдите сумму цифр трехзначного числа.
"""
num = ''
def main():
    global num
    while True:
        num = input("Введите число или 'Q' для завершения программы:")
        if num == 'Q':
            exit()
        else:
            check_input()
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
            num = int(num)
            return num
        except:
            print('Введеное значание не является типом int!')
            num = input("Введите новое число или 'Q' для завершения программы:")
            if num == 'Q':
                exit()

main()

