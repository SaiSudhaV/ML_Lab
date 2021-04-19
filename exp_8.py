# 8 python program to display a multiplication table

def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
    return

if __name__ == "__main__":
    n = int(input())
    multiplication_table(n)