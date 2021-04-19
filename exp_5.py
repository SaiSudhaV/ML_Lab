# 5 python program to check prime number
from math import sqrt

def is_prime(n):
    res = [i for i in range(2, int(sqrt(n)) + 1) if n % i == 0]
    return "composite" if res else "prime"

if __name__ == "__main__":
    n = int(input())
    print(is_prime(n))