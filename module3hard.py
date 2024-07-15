def calculate_structure_sum(data_structure):
    global data_structure_sum
    if len(data_structure) != 0:
        for x in data_structure:
            if type(x) is list or type(x) is tuple:
                data_structure_sum = calculate_structure_sum(x)
            if type(x) is dict:
                x_items = list(x.items())
                data_structure_sum = calculate_structure_sum(x_items)
            if type(x) is str:
                len_x = len(x)
                data_structure_sum += len_x
            if type(x) is int:
                data_structure_sum += x
    return (data_structure_sum)

data_structure = [
 [1, 2, 3],
 {'a': 4, 'b': 5},
 (6, {'cube': 7, 'drum': 8}),
 "Hello",
 ((), [[(2, 'Urban', ('Urban2', 35))]])
]
data_structure_sum = 0
result = calculate_structure_sum(data_structure)
print(result)