print('1')
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    print("Меньшее число:", a)
else:
    print("Меньшее число:", b)

print('2')
x = int(input("Введите число: "))
if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

print('3')
n = int(input("Введите число N: "))
s = 0
for i in range(1, n+1):
    s += i
print("Сумма от 1 до", n, "=", s)

print('4')
n = int(input("Введите число для таблицы умножения: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

print('5')
n = int(input("Введите число N: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Факториал:", fact)

print('6')
s = input("Введите строку: ")
vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Количество гласных:", count)

print('7')
s = input("Введите строку: ")
print("Разворот:", s[::-1])

print('8')
arr = list(map(int, input("Введите массив чисел через пробел: ").split()))
print("Максимум:", max(arr))

print('9')
print("Сумма элементов массива:", sum(arr))

print('10')
x = int(input("Введите число для поиска: "))
if x in arr:
    print("Число найдено в массиве")
else:

    print("Число отсутствует в массиве")
