from typing import List

if __name__ == "__main__" :
    n = int(input().rstrip())
    dp : List[int] = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1) :
        for k in range(i) :
            dp[i] += dp[k] * dp[i - k - 1]

    print(dp[n])