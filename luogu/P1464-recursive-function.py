from typing import List, Dict

memory : Dict[str, int] = {}

def recursive(a : int, b : int, c : int) -> int :
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20 :
        return recursive(20, 20, 20)
    elif f"{a} {b} {c}" in memory :
        return memory[f"{a} {b} {c}"]
    elif a < b and b < c :
        res = recursive(a, b, c - 1)     \
            + recursive(a, b - 1, c - 1) \
            - recursive(a, b - 1, c)
        memory[f"{a} {b} {c}"] = res
        return res
    else :
        res = recursive(a - 1, b, c)        \
            + recursive(a - 1, b - 1, c)    \
            + recursive(a - 1, b, c - 1)    \
            - recursive(a - 1, b - 1, c - 1)
        memory[f"{a} {b} {c}"] = res
        return res

if __name__ == "__main__" :
    while True :
        a, b, c = tuple(map(int, input().rstrip().split(" ")))
        if a == -1 and b == -1 and c == -1 :
            break
        else :
            print(f"w({a}, {b}, {c}) = {recursive(a, b, c)}")