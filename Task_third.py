# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


def gess_num():
    num = randint(0, 1000)
    print(num)
    n = int(input("Угадай число от 0 до 1000 включительно за 10 попыток.Введите число: "))
    count = 9
    while count:
        count -= 1
        if n == num:
            print("Поздравляем! Вы угадали.")
            break
        elif n < num:
            n = int(input("Недолет. Попробуйте еще раз: "))
        else:
            n = int(input("Перелет. Попробуйте еще раз: "))
    else:
        print("Вы исчерпали число попыток.")


gess_num()
