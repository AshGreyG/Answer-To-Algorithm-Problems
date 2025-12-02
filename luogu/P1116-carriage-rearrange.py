from typing import List

def bubble_sort_swaps(array : List[int]) -> int :
    k = len(array)
    r = 0
    for i in range(k) :
        for j in range(k - i - 1) :
            if array[j] > array[j + 1] :
                r += 1
                array[j], array[j + 1] = array[j + 1], array[j]
    return r

if __name__ == "__main__" :
    n = int(input().rstrip())
    numbers : List[int] = []

    while True :
        try :
            line = input().rstrip()
            if line != "" :
                numbers.extend(list(map(int, line.split(" "))))
            else :
                raise EOFError
        except EOFError :
            break

    print(bubble_sort_swaps(numbers))