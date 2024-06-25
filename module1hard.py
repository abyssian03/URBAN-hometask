grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list = sorted(students)
my_dict = {}
i = 0
if len(list) != len(grades):
    print ("Несоответствие списков, подсчет не может быть завершен.")
else:
    for name in list:
        my_dict.update({name: sum(grades[i])/len(grades[i])})
        i = i + 1
#другой вариант
#else:
#         my_dict.update({sorted(students)[x] : sum(grades[x])/len(grades[x]) for x in range(len(grades))})
print(my_dict)