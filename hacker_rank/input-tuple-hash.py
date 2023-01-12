# Sample input:
# 1
# 1 2

if __name__ == '__main__':
    N = int(input())        # N -> number of integers
    # the integers seperated by space -> transformed to a list
    #
    integer_list = list(map(int, input().split(" ")))

    # print(li)
    t = tuple(integer_list)
    # print(t)
    print(hash(t))
