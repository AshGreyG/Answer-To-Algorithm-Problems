def cantor(n : int) -> str :
    p = 1
    q = 1
    count = 1
    direction = True

    while count != n :
        if p == 1 and q % 2 == 1 :
            q += 1
            direction = True
        elif q == 1 and p % 2 == 0 :
            p += 1
            direction = False
        elif direction :
            p += 1
            q -= 1
        else :
            p -= 1
            q += 1
        count += 1

    return f"{p}/{q}"

if __name__ == "__main__" :
    n = int(input().rstrip())
    print(cantor(n))