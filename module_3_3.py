def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 3, 4)
print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = [12, 'github', [True, False]]
values_dict = {'a': 'Привет, ребята!', 'b': 0, 'c': [1, 0]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 5.0]
print_params(*values_list_2, 42)

