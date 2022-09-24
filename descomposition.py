# primes list from 1 to 30
primes = [2,3,5,7,11,13,17,19,23,29]
# frequency list of primes
frequency = [0,0,0,0,0,0,0,0,0,0]
number = int(input("Write your number\n"))

index = 0
for prime in primes:
    while number % prime == 0:
        frequency[index] += 1
        number = number / prime
    index += 1
    if number == 1:
        break
print("last index:",index)
        
print(frequency)
        