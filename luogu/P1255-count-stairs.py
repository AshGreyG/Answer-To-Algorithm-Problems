from typing import List

# T(n) = T(n - 1) + T(n - 2), n >= 2

if __name__ == "__main__" :
    n = int(input().rstrip())

    if n == 1 :
        print("1")
        exit()
    elif n == 2 :
        print("2")
        exit()

    methods : List[int] = [0] * n
    methods[0] = 1
    methods[1] = 2

    for i in range(2, n) :
        methods[i] = methods[i - 1] + methods[i - 2]

    print(methods[n - 1])