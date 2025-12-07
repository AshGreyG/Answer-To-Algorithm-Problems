from typing import List

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def bbase_sum(m : str, n : str, base : int) -> str :
    bbase_digits = digits[0:base]
    m = m[::-1]
    n = n[::-1]

    d = lambda s : bbase_digits.find(s)
    s = lambda d : bbase_digits[d]

    maxs : List[int] = []
    mins : List[int] = []
    if len(m) >= len(n) :
        maxs = list(map(d, m))
        mins = list(map(d, n))
    else :
        maxs = list(map(d, n))
        mins = list(map(d, m))

    res_array = maxs.copy()
    res_array.append(0)

    for i in range(len(res_array) - 1) :
        if i < len(mins) :
            current = res_array[i] + mins[i]
            if current >= base :
                res_array[i + 1] += current // base
                res_array[i] = current % base
            else :
                res_array[i] = current
        else :
            current = res_array[i]
            if current >= base :
                res_array[i + 1] += current // base
                res_array[i] = current % base

    res = "".join(map(s, res_array))[::-1].lstrip("0")

    return res if len(res) != 0 else "0"

if __name__ == "__main__" :
    b = int(input().rstrip())
    m = input().rstrip()
    n = input().rstrip()

    print(bbase_sum(m, n, b))