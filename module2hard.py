data = int(input("Заданное число: "))
parole = '*'
for i in range(1, 20):
    for j in range(1, 20):
        if i != j and not '*' + str(j) + ',' + str(i) + '*' in parole and data % (i + j) == 0:
             parole = parole +  str(i) + ',' + str(j) + '*'
parole = parole.replace(',', '')
parole = parole.replace('*', '')
print ("Пароль", parole)

