# PROBLEM
# from inputs x, y, z representing the dimension of a cuboid, along with input n
# print a list of all possible coordinate (i,j,k) on s 3d grid if i+j+k != n
# where 0<=i<=x, 0<=j<=y, 0<=k<=z
# print the list in a lexicographic increasing order

# Test case:
#     input: 1,1,2,3
#     Output: [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

# Test case:
#     input: 2,2,2,2
#     Output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i_arr = [i for i in range(x + 1)]
    j_arr = [j for j in range(y + 1)]
    k_arr = [k for k in range(z + 1)]
    # print(i_arr)
    # print(j_arr)
    # print(k_arr)

    the_arr = [[i, j, k] for i in i_arr
                           for j in j_arr
                           for k in k_arr
                            if not i + j + k == n]

    # print(the_arr)

    arr = [the_arr[idx] for idx in range(0, len(the_arr))]
    print(arr)
    # for i in range(0, len(arr)):
    # Initially sorting the array row-wise
    # arr[i].sort()

    # for i in range(0, len(arr)) :
    #     for j in range(0, len(arr[i])) :
    #         print(arr[i][j] , end = " ")