from typing import List

if __name__ == "__main__" :
    n, m = tuple(map(int, input().rstrip().split(" ")))
    foods = list(map(int, input().rstrip().split(" ")))
    dp : List[List[int]] = []

    for _ in range(n + 1) :
        row = []
        for _ in range(m + 1) :
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1) :
        for j in range(1, m + 1) :
            if j == foods[i - 1] :
                dp[i][j] = dp[i - 1][j] + 1
            elif j > foods[i - 1] :
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - foods[i - 1]]
            else :
                dp[i][j] = dp[i - 1][j]

    print(dp[n][m])