__Author__ = 'Ryan Cabrera'


def main():
    lst_hundred_integers = range(1, 101)
    for i in lst_hundred_integers:
        if i % 3 == 0 and i % 5 == 0:
            print(i, ": FizzBuzz")
        elif i % 3 == 0:
            print(i, ": Fizz")
        elif i % 5 == 0:
            print(i, ": Buzz")


if __Author__:
    main()
