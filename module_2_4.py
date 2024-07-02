numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num == 1 or num == 2:
        primes.append(num)
    else:
        for j in range(2, num):
            if num % j != 0:
                is_prime = True
            else:
                is_prime = False
                break
        if is_prime == True:
            primes.append(num)
        else:
            not_primes.append(num)
print ("Простые: ", primes)
print ("Не простые: ", not_primes)