# Задача №2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите значения x: '))
Y = int(input('Введите значения y: '))
Z = int(input('Введите значения z: '))

if (not (X or Y or Z)) == (not X and not Y and not Z):
    print("True")
else:
    print("False")