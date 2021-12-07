import time as t
from sympy import sieve

def main():
    start = t.time()
    max = 2000000
    prime_list = list(sieve.primerange(1,2000000))
    sum_primes = sum(prime_list)
    print(sum_primes)
    end = t.time()
    print("Runtime = ", end-start)


if __name__ == "__main__":
    main()