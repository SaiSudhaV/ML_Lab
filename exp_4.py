# 4 python program to find largest among three numbers

def maxOf3(a, b, c):
    # return a if a > b and a > c else b if b > c else c
    return max(a, b, c)

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(maxOf3(a, b, c))