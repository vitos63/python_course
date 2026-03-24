# name = input("Введите ваше имя: ")
# print("Привет,", name)


# age = input("Введите ваш возраст: ")
# print("Ваш возраст:", age)


# a = 6
# b = 3

# print(a + b)  # сложение
# print(a - b)  # вычитание
# print(a * b)  # умножение
# print(a / b)  # деление

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# print("Сложение:", a + b)


# num_1 = 17
# num_2 = 18

# s_1 = str(num_1)
# s_2 = str(num_2)


# print(num_1 + num_2)
# print(s_1 + s_2)

# print(3**0)
# print(2**2)
# print(4**0.5)
# print(5**(-1))
# print((-3)**(-2))


# print(12 // 10)
# print(105 // 4)
# print(145 // 10)
# print(10.5 // 10)

# print(12 % 10)
# print(105 % 4)
# print(145 % 10)
# print(10.5 % 10)


# Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
# 12 => 21
# 45 => 54

# num = int(input())
# last_digit = num % 10 # 2
# first_digit = num // 10 # 1
# print(last_digit*10 + first_digit)


# Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через пробел).
# 789 => 7 8 9
# 123 => 1 2 3

num = int(input())

digit3 = num % 10
digit1 = num // 100
digit2 = (num // 10) % 10
print(digit1, digit2, digit3)