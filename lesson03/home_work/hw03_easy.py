# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    round_number = 10 ** ndigits
    number_2 = int(number * round_number + 0.5)
    scale_number = number_2 / round_number
    return scale_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    lst_1 = list(str(ticket_number))
    lst_2 = []
    lst_2.append(lst_1[3:6])
    del lst_1[3:6]
    lst_1 = [int(i) for i in lst_1]
    lst_2 = [int(el) for el in lst_2]
    if lst_1[0] + lst_1[1] + lst_1[2] == lst_2[0] + lst_2[1] + lst_2[2]:
        print('У вас счастливый билет!')
    else:
        print('У вас обычный билет')
        # Не могу понять в чем ошибка, логика программы вроде бы правильная :(


print(lucky_ticket(123006))
print(lucky_ticket(436751))
