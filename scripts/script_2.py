"""An Example to showcase the entry points of python execution"""


def add(num_1, num_2):
    print("I'm from the add Function")
    return num_1 + num_2


def main():
    a = 10
    b = 20
    print("I'm from the main function")
    sum = add(a, b)
    print("Sum : " + str(sum))
    return sum


if __name__ == "__main__":
    print("I'm the first line of the script")
    main()
    print("I'm the last line of the script")
