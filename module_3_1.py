def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    x = [len(string), string.upper(), string.lower()]
    return (x)

def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return (True)
    else:
        return (False)

calls = 0
choice1 = 'y'
choice2 = 'y'
while choice2 == 'y':
    string = input("Введите слово: ", )
    print('Результат операций со словом:', string_info(string))
    choice1 = input('Продолжить? (y/n) ', )
    if choice1 == 'y':
        list_to_search = list(input("Введите список слов, разделяя пробелами: ", ).lower().split(" "))
        print('Проверка наличия слова в списке:', is_contains(string.lower(), list_to_search))
        choice2 = input('Продолжить? (y/n) ', )
    else:
        break

print("Количество вызовов функций: ", calls)