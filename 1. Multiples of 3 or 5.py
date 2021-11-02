
def multiples_of_3_or_5(max):
    sum = 0
    for i in range(max):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum


def main():
    sum1000 = multiples_of_3_or_5(1000)
    print(sum1000)

if __name__ == "__main__":
    main()   