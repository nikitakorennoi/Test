'''Даны целые положительные числа А и В (А > В). На отрезке длины А
размещено максимально возможное количество отрезков длины В (без наложений).
Используя операцию деления нацело, найти количество отрезков В, размещенных на отрезке А.'''

otrezokA = int(input("Vvedite dlinu otrezka A: "))
otrezokB = int(input("Vvedite dlinu otrezka B: "))
kolichestvo = otrezokA // otrezokB
print(f"Kolichestvo otrezkov B v otrezke A: {kolichestvo}")
