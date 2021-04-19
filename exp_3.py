# 3 python program to check leap year

def is_leap(n):
    return "leap year" if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else "non-leap year"

if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))