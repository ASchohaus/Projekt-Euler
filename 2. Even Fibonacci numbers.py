
def even_fibonacci_numbers(max):
    i_n1 = 1
    i_n2 = 2
    sum = i_n2
    while(sum != 0):
        i_n3 = i_n1 + i_n2
        if i_n3 >= max:
            return sum
        if i_n3 % 2 == 0:
            sum += i_n3
        i_n1 = i_n2
        i_n2 = i_n3
       


def main():

    sum4e6 = even_fibonacci_numbers(4e6)
    print(sum4e6)


if __name__ == "__main__":
    main()