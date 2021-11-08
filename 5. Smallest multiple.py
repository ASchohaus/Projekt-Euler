import time as t

def multiple_find(num, max_multiple):
    is_multiple = True
    for i in range(1, max_multiple):
        is_multiple = is_multiple and (num % (max_multiple - i) == 0)
        if is_multiple == False:
            return is_multiple
    return is_multiple

def find_smallest_multiple(max_multiple):
    i = 20
    while(multiple_find(i, max_multiple) == False):
        i += 20
    return i



def main():
    start = t.time()
    max_multiple_of_20 = find_smallest_multiple(20)
    print(max_multiple_of_20)
    end = t.time()
    print("Runtime = ", end-start)



if __name__ == "__main__":
    main()