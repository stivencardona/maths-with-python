primes = [2,3,5,7,11,13,17,19,23,29]

def find_primes(number):
    frequency = [0,0,0,0,0,0,0,0,0,0]
    index = 0
    for prime in primes:
        while number % prime == 0:
            frequency[index] += 1
            number = number / prime
        index += 1
        if number == 1:
            break
    return frequency

number_one = int(input())
number_two = int(input())
primes_number_one = find_primes(number_one)
primes_number_two = find_primes(number_two)

gcd = 1
index = 0
for prime_one, prime_two in zip(primes_number_one,primes_number_two):
    gcd *= primes[index] ** min(prime_one,prime_two)
    index += 1

print(gcd)