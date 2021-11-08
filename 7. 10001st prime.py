import time as t
import sympy as sy


def main():
    start = t.time()
    print(sy.prime(10001))
    end = t.time()
    print("Runtime = ", end-start)


if __name__ == "__main__":
    main()