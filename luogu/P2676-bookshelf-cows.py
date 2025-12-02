from typing import List

if __name__ == "__main__" :
    n, b = tuple(map(int, input().rstrip().split(" ")))
    heights : List[int] = []

    for _ in range(n) :
        heights.append(int(input().rstrip()))

    heights.sort(reverse = True)

    sumh = 0
    cnth = 0
    for h in heights :
        sumh += h
        cnth += 1
        if sumh >= b :
            print(cnth)
            break