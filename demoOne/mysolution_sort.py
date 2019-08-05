__Author__ = 'Ryan Cabrera'


def sort(some_list):
    for index in range(0, len(some_list)-1):
        if some_list[index] > some_list[index+1]:
            some_list[index], some_list[index+1] = some_list[index+1], some_list[index]
            sort(some_list)

    return some_list


def main():
    nums = [5, 4, 6, 123, 4, 0, -1]
    for n in sort(nums):
        print(n)


if __Author__:
    main()