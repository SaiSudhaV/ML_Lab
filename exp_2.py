# 2 python program to check a number is odd or even

def even_or_odd(n):
    return "odd" if n % 2 else "even"

if __name__ == "__main__":
    n = int(input())
    print(even_or_odd(n))