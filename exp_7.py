# 7 python program to find factorial of a number

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input())
    print(factorial(n))