 #Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
 
 # ************************
def Fibonachchi(dig):
    listFib = []
    a, b = 1, 1
    for i in range(dig-1):
        listFib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (dig):
        listFib.insert(0, a)
        a, b = b, a - b
    return listFib

#************************
import os 
os.system('cls')

print("Программа составляет список чисел Фибоначчи, в том числе для отрицательных индексов, от заданного числа.")
digit = int(input("Введите число: "))

listFib = Fibonachchi(digit)

print(f"Список чисел Фибоначчи: {listFib}")