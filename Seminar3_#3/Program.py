 #Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#************************
def fillList(n,l,r):
    import random
    resultList = []
    for i in range(n):
        resultList.append(round(random.uniform(l, r),2))

    return resultList

#************************
def listdifference(lst):
    lstcomp = []
    for i in lst:
        lstcomp.append(int((i % 1)*100))
    return (max(lstcomp) - min(lstcomp))/100

#************************
import os 
os.system('cls')

print("Программа задает список из вещественных чисел и находит разницу между максимальным и минимальным значением дробной части элементов.)")
listN = int(input("Введите размерность списка: "))
listL = float(input("Введите начало диапазона вещественных чисел для заполнения списка: "))
listR = float(input("Введите окончание диапазона вещественных чисел для заполнения списка: "))

lst = fillList(listN, listL, listR)
diff = listdifference(lst)

print(f"В списке {lst} разница между максимальным и минимальным значением дробной части элементов: {diff}")