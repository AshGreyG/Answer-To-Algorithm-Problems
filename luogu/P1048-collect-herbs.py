from typing import List

class Herb :
    def __init__(self, time : int, value : int) -> None :
        self.time = time
        self.value = value

if __name__ == "__main__" :
    herbs : List[Herb] = []
    time, herb_amount = map(int, input().rstrip().split(" "))

    for i in range(herb_amount) :
        herb_time, herb_value = map(int, input().rstrip().split(" "))
        herbs.append(Herb(herb_time, herb_value))

    dp : List[List[int]] = []

    for _ in range(herb_amount + 1) :
        row = []
        for _ in range(time + 1) :
            row.append(0)
        dp.append(row)

    for i in range(1, herb_amount + 1) :
        for j in range(1, time + 1) :
            if j >= herbs[i - 1].time :
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - herbs[i - 1].time] + herbs[i - 1].value)
            else :
                dp[i][j] = dp[i - 1][j]

    print(dp[herb_amount][time])