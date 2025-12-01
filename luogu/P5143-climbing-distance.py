from typing import List, Tuple

import math

if __name__ == "__main__" :
    n = int(input().rstrip())
    points : List[Tuple[int, int, int]] = []
    distance = 0.0

    for _ in range(n) :
        p = list(map(int, input().rstrip().split(" ")))
        points.append((p[0], p[1], p[2]))

    points.sort(key = lambda p : p[2])

    for i in range(1, n) :
        distance += math.sqrt(
            (points[i][0] - points[i - 1][0]) ** 2 +
            (points[i][1] - points[i - 1][1]) ** 2 +
            (points[i][2] - points[i - 1][2]) ** 2
        )

    print(f"{distance:.3f}")