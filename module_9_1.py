from math import sqrt

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return(results)

def get_prime(int_list):
    result = []
    for num in int_list:
        flag = True
        for n in range(2, num):
            if num % n == 0:
                flag = False
                break
        if flag == True:
            result.append(num)
    return (result)

def get_square(int_list):
    result = [num for num in int_list if sqrt(num) % 1 == 0]
    return (result)

def get_monodigital(int_list):
    result = []
    for num in int_list:
        flag = True
        i = 1
        while num // (10 ** i) != 0:
            flag = False
            n1 = num % (10 ** i)
            n2 = (num % (10 ** (i+1))) // 10
            if n1 == n2:
                flag = True
            i += 1
        if flag == True:
            result.append(num)
    return (result)

my_list = [1, 2, 3, 6, 9, 11, 12, 13, 111, 121, 112, 222]
my_functions = [get_prime, get_square, get_monodigital]
print(apply_all_func(my_list, *my_functions))
