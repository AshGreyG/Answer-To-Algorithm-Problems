from typing import List
from functools import cmp_to_key

n = int(input().rstrip("\r\n"))

numbers = input().rstrip("\r\n").split(" ")

# WTF, this problem luogu uses Windows to write test points... So we must
# strip the `\r\n` first

def largest_number(nums : List[str]) -> str :
    def compare(a : str, b : str) -> int :
        if a + b > b + a :
            return -1
        else :
            return 1

    nums.sort(key = cmp_to_key(compare))

    return "".join(nums)

print(largest_number(numbers))
