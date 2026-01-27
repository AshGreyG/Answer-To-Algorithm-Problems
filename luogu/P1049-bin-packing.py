from typing import List

# Total volume 'tv', every item has its "weight" 'volumes[i]' and "value"
# 'volumes[i]'.

if __name__ == "__main__" :
    tv = int(input().rstrip())
    n  = int(input().rstrip())
    volumes : List[int] = []
    dp : List[int] = [0] * (tv + 1)

    for i in range(n) :
        v = int(input().rstrip())
        volumes.append(v)

    for i in range(n) :
        for j in range(tv, volumes[i] - 1, -1) :
            dp[j] = max(dp[j], dp[j - volumes[i]] + volumes[i])

    print(tv - dp[tv])