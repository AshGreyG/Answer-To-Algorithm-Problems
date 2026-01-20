from typing import List

class Carpet :
    def __init__(
        self, 
        a : int,
        b : int,
        g : int,
        k : int
    ) -> None :
        self.a = a
        self.b = b
        self.g = g
        self.k = k

if __name__ == "__main__" :
    carpets : List[Carpet] = []
    index = -1

    n = int(input().rstrip())

    for i in range(n) :
        carpet_info = list(map(int, input().rstrip().split(" ")))
        carpet = Carpet(
            carpet_info[0],
            carpet_info[1],
            carpet_info[2],
            carpet_info[3],
        )
        carpets.append(carpet)

    x, y = map(int, input().rstrip().split(" "))

    for i, carpet in enumerate(carpets) :
        if  carpet.a <= x <= carpet.a + carpet.g - 1 and \
            carpet.b <= y <= carpet.b + carpet.k - 1 :
            index = i + 1

    print(index)