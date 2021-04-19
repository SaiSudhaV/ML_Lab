# 6 python program to print all prime numbers in given interval

from math import sqrt

def check_prime(n):
    res = [i for i in range(2, int(sqrt(n)) + 1) if n % i == 0]
    return False if res else True

def gen_primes(start, end):
    return [i for i in range(start, end + 1) if check_prime(i)]

if __name__ == "__main__":
    start, end = map(int, input().split())
    print(gen_primes(start, end))