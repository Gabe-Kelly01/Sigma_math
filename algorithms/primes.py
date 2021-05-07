from math import isqrt

def check_prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False

    r = int(n**0.5)
    f = 5

    while f <= r:
        print('\t',f)
        if n%f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    
    return True

def generate_primes(bound: int, display: bool) -> list:
    if bound <= 2:
        return []

    is_prime = [True] * bound
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(bound)+1):
        if is_prime[i]:
            for x in range(i*i, bound, i):
                is_prime[x] = False
    
    results =  [i for i in range(bound) if is_prime[i]]
    if display: print(results)
    return results

if __name__ == '__main__':
    import time
    
    start = time.perf_counter()
    print(len(generate_primes(10000000, False)))
    elapsed = time.perf_counter() - start
    print(f'Completed in {elapsed:.2f}s')


