def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        for i in range(2, result):
            if result % i == 0:
                print("Составное")
                return (result)
        print("Простое")
        return (result)
    return wrapper

@is_prime
def sum_three(first, second, third):
    result = first + second + third
    return result

sum_three(5, 6, 8)