import time as t

def data_to_array(data_name):
    a = []
    data = open(data_name, 'r')
    first = data.read(1)
    print(first)


    data.close()
    return a



def main():
    start = t.time()
    data_name = 'C:\Users\miste\Desktop\Programmiern\Projekt Euler\textfor8.txt'
    data_to_array(data_name)

    end = t.time()
    print("Runtime = ", end-start)


if __name__ == "__main__":
    main()