"""List of prime numbers generator."""

from math import sqrt, floor

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError("Number of primes must not be lower than 1.")

    list = [2]
    i = 1
    count = 1

    while count < number_of_primes:
        i += 2
        for k in range(2, 1+floor(sqrt(i+1))):
            if i%k == 0:
                break
        else:
            list.append(i)
            count += 1

    return list

print(primes(100))