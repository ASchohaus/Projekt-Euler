import time as t

def find_sum_of_pythagorean_triplet(sum):
    for i in range(1, sum):
        a = i
        for j in range(i, sum):
            b = j + 1
            c = sum - a - b
            if (a**2 + b**2 == c**2):
                print(a, b, c)
                return a*b*c


def main():
    start = t.time()
    sum = 1000
    product_triplet = find_sum_of_pythagorean_triplet(1000)
    print(product_triplet)
    end = t.time()
    print("Runtime = ", end - start)


if __name__ == "__main__":
    main()