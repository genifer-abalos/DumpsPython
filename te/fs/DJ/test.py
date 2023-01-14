def lambdaMap(arr):
    ans = map(
        # Complete the lambda function below.  It begins in the non-alterable code above
        lambda x: [pow(i,2) for i in x if i>=0], arr
    )
    return ans


if __name__ == '__main__':
    # n = int(input())
    n = 2
    arr = []
    # arr = [[-1, 1, 2, -2, 6], [3, 4, -5]]

    for _ in range(1):
    #     arr.append(list(map(int, input().split())))
        arr.append(list(map(int, "-1 1 2 -2 6".split())))
        arr.append(list(map(int, "3 4 -5".split())))

    # print(arr)

    ans = lambdaMap(arr)
    for row in ans:
        print(' '.join(map(str, row)))


# # Input
# 2
# -1 1 2 -2 6
# 3 4 -5

# goal
# remove the negatives
# then square the values