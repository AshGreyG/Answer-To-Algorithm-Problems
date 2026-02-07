from typing import List

def represent_with02(n : int) -> str :
    if n == 0 :
        return "2(0)"
    elif n == 1 :
        return "2"
    elif n == 2 :
        return "2(2)"

    binary = bin(n)[2:]

    indexes : List[int] = []
    for i in range(len(binary)) :
        if binary[i] == "1" :
            indexes.append(len(binary) - 1 - i)

    res = ""
    for i, idx in enumerate(indexes) :
        if idx != 0 and idx != 1 and idx != 2 :
            res += f"2({represent_with02(idx)})"
        else :
            res += represent_with02(idx)
        if i != len(indexes) - 1 :
            res += "+"
    return res

if __name__ == "__main__" :
    n = int(input().rstrip())
    print(represent_with02(n))