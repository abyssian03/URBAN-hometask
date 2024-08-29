first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zipped = list(zip(first, second))
first_result = [abs(len(pair[0])-len(pair[1])) for pair in zipped if len(pair[0]) != len(pair[1])]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
print(first_result, second_result)