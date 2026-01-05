#1
print("Привет!")

#2
name = input("Ваше имя: ")
print(f"Привет, {name}")

#3
a = float(input("Первое число: "))
b = float(input("Второе число: "))
print("Сумма чисел:", a + b)


#4
a = float(input("Первое число: "))
b = float(input("Второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)
print("Частное:", a / b)
print("Целочисленное деление:", a // b)
print("Остаток:", a % b)
print("Степень:", a ** b)


#5
n = int(input("Число: "))
if n % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")


#6
n = float(input("Число: "))
if n > 0:
    print("Положительное")
elif n < 0:
    print("Отрицательное")
else:
    print("Ноль")



#7
n = int(input("Число: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)



#8
n = int(input("Число: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Факториал:", fact)



#9
n = int(input("Число: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Простое число")
else:
    print("Не простое число")



#10
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

print("Минимум:", min(a, b, c))
print("Максимум:", max(a, b, c))