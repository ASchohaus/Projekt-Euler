import time as t
import sympy as sy

#To find the largest prime factor, start dividing the number by the smallest prime number until u find the smallest prime factor.
#Repeat the process for the qoutient and repeat it until the quotient becomes 1. Then u have the smallest prime factor.
def largest_prime_factor(max):
    i = 1
    while (max != sy.prime(i)):
        if max % sy.prime(i) == 0:
            max = max / sy.prime(i)
        else:
            i += 1
    return sy.prime(i)


def main():
    start = t.time()
    prime600851475143 = largest_prime_factor(600851475143)
    print(prime600851475143)
    end = t.time()
    print("Runtime = ", end-start)


if __name__ == "__main__":
    main()