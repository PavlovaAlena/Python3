 #Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#************************
def fillList(n,l,r):
    import random
    resultList = []
    for i in range(n):
        resultList.append(random.randint(l, r))

    return resultList

#************************
def listcomposition(lst):
    if len(lst) % 2 != 0:
        l = len(lst)//2 + 1
    else: l = len(lst)//2
    lstcomp = []
    for i in range(l):
        lstcomp.append(lst[i]*lst[len(lst)-i-1])
    return lstcomp

#************************
import os 
os.system('cls')

print("Программа задает список из нескольких чисел и находит произведение пар чисел списка (первый и последний элемент, второй и предпоследний и т.д.)")
listN = int(input("Введите размерность списка: "))
listL = int(input("Введите начало диапазона чисел для заполнения списка: "))
listR = int(input("Введите окончание диапазона чисел для заполнения списка: "))

lst = fillList(listN, listL, listR)
lstcomp = listcomposition(lst)

print(f"Из списка {lst} путем умножения элементов получен: {lstcomp}")