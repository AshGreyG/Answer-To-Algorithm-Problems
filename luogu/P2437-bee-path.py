from typing import List

if __name__ == "__main__" :
    m, n = tuple(map(int, input().rstrip().split(" ")))
    dp : List[int] = [0] * (n - m + 1)
    dp[0] = 1
    if n - m + 1 > 1 :
        dp[1] = 1

    for i in range(2, n - m + 1) :
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n - m])