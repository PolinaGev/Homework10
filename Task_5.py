# Задача №5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


xa = int(input('Введите xa: '))
ya = int(input('Введите ya: '))
xb = int(input('Введите xb: '))
yb = int(input('Введите yb: '))

itog = ((xb - xa) ** 2 + (yb - ya) ** 2) ** (0.5)
print(itog)