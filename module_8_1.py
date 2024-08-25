def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    return (result)

print(add_everything_up(2, 5))
print(add_everything_up('b', 5))
