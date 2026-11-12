n = int(input("Enter number: "))

is_n_prime = True

if n < 2:
    is_n_prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_n_prime = False
            break
        i += 1

if is_n_prime:
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")


primes = []
total = 0
current = 2

while current <= n:

    is_prime = True
    if current < 2:
        is_prime = False
    else:
        j = 2
        while j * j <= current:
            if current % j == 0:
                is_prime = False
                break
            j += 1
    
    if is_prime:

        primes.append(current)
        total = total + current
    
    current += 1

print(f"Primes up to {n}: {primes}")
print(f"Sum of primes: {total}")