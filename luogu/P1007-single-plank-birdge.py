from typing import List

def min_time(bridge : int, pos : List[int]) -> int :
    """
    This function returns the minimum consumption of soldiers leaving the single
    plank bridge. And that's the situation :

        +---+---+-----+---+-------+-----+---+
     0  | 1 | 2 | ... | m | m + 1 | ... | N | N + 1
        +---+---+-----+---+-------+-----+---+
                        ↑
    when soldier at position 'm' has a shorter path to left '0' then 'N+1', then
    soldiers at left of him also goes to left. We only to check who is closest
    to the center!
    """

    min = 0
    for p in pos :
        if p >= bridge - p + 1 and bridge - p + 1 >= min :
            min = bridge - p + 1
        elif p < bridge - p + 1 and p >= min :
            min = p
    return min

def max_time(bridge : int, pos : List[int]) -> int :
    """
    Question says that if two soldiers encounter each other, they will turn back
    and this process doesn't consume any time ! So it's equal to they actually
    go through each other.
    """

    max = 0
    for p in pos :
        if p >= bridge - p + 1 and p >= max :
            max = p
        elif p < bridge - p + 1 and bridge - p + 1 >= max :
            max = bridge - p + 1
    return max

if __name__ == "__main__" :
    bridge = int(input().rstrip())
    soldiers = int(input().rstrip())
    if soldiers != 0 :
        soldiers_pos : List[int] = list(map(int, input().rstrip().split(" ")))
        print(f"{min_time(bridge, soldiers_pos)} {max_time(bridge, soldiers_pos)}")
    else :
        print("0 0")