import time as t

def sum_of_squares(max):
    sum = 0
    for i in range(1, max + 1):
        sum += i**2
    return sum

def square_of_sum(max):
    sum = 0
    for i in range(1, max + 1):
        sum += i
    return sum**2




def main():
    start = t.time()
    max = 100
    sum_difference = square_of_sum(max) - sum_of_squares(max)
    print(sum_difference)
    end = t.time()
    print("Runtime = ", end-start)

if __name__ == "__main__":
    main()