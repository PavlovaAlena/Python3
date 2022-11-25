 #Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное

#************************
def digit_binary(dig):
    res = ""
    while dig != 0:
        res = str(dig%2) + res
        dig //=2
    return res

#************************
import os 
os.system('cls')

print("Программа преобразовывать десятичное число в двоичное.)")
digit = int(input("Введите число для преобразования в двоичное: "))

binary = digit_binary(digit)

print(f"Десятичное число {digit} в двоичном виде: {binary}")