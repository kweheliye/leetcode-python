import string
import itertools

# add return type to the function hint
def letters() -> str:
    """Generate the lowercase letters 'a' to 'z'."""
    for c in string.ascii_lowercase:
        yield c

def prime_numbers():
    """Generate prime numbers."""
    # Sieve of Eratosthenes
    yield 2
    prime_cache = [2]
    for n in itertools.count(3,2):
        is_prime = True
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n


for p in prime_numbers():
    print(p)
    if p > 100:
        break


def generate_numbers(n):
    for i in range(n):
        yield i  # Pause here and return the current value
gen = generate_numbers(5)
print(next(gen))


# for letter in letters():
#     print(letter)