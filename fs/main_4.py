def multiply(a, b, bound):
    # write your code here
    ab = a * b
    print(ab)
    if ab <= bound:
        return ab
    if ab > bound:
        raise ValueError(f"if a={a}")


if __name__ == '__main__':
    multiply(4,5,20)