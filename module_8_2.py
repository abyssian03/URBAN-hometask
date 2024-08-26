def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            result += number
    except TypeError:
        incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        return (personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1]))
    except ZeroDivisionError:
        return (0)
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(calculate_average([3, 4, 5]))
print(calculate_average([1, 2, 7, 'b']))
print(calculate_average(['b']))
print(calculate_average(5))