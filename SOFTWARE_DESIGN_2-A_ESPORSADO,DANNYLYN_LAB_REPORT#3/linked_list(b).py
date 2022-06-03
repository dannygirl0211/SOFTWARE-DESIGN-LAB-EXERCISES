
def add(A, B, m, n):
    size = max(m, n);
    sum = [0 for i in range(size)]

    for i in range(0, m, 1):
        sum[i] = A[i]

    for i in range(n):
        sum[i] += B[i]

    return sum


def print_poly(poly, n):
    for i in range(n):
        print(poly[i], end="")
        if (i != 0):
            print("x^", i, end="")
        if (i != n - 1):
            print(" + ", end="")


if __name__ == '__main__':
    A = [3, 5, 7, 9]
    B = [2, 4, 8, 16]
    m = len(A)
    n = len(B)

    print("First polynomial is")
    print_poly(A, m)
    print("\n", end="")
    print("Second polynomial is")
    print_poly(B, n)
    print("\n", end="")

    sum = add(A, B, m, n)
    size = max(m, n)

    print("Sum polynomial is")
    print_poly(sum, size)
