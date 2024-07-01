first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
third = int(input("Введите третье число:"))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(25)
else:
    print3(0)