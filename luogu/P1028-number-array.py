from typing import List

# dp[n] = \sum_{i=1}^{n / 2} dp[i]

if __name__ == "__main__" :
    n = int(input().rstrip())
    dp : List[int] = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1) :
        for j in range(i // 2 + 1) :
            dp[i] += dp[j]

    print(dp[n])