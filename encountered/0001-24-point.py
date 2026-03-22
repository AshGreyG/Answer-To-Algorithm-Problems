from itertools import permutations, product
from typing import List

ops = ["+", "-", "*", "/"]

def solve24(nums : List[int]) -> None :
    """
    This function solves the 24-point puzzle, for example, input is a list
    [2, 3, 4, 5], then it will find the expression using operators { +, -, *, / }
    and operands { 2, 3, 4, 5 } to make 24.
    """

    for a, b, c, d in permutations(nums) :
        for op1, op2, op3 in product(ops, ops, ops) :
            exps = [
                f"( ( {a} {op1} {b} ) {op2} {c} ) {op3} {d}", # ((a + b) - c) + d
                f"( {a} {op1} {b} ) {op2} ( {c} {op3} {d} )", # (a + b) - (c + d)
                f"{a} {op1} ( ( {b} {op2} {c} ) {op3} {d} )", # a + ((b - c) + d)
                f"{a} {op1} ( {b} {op2} ( {c} {op3} {d} ) )"  # a + (b - (c + d))
            ]
            for exp in exps :
                try :
                    if eval(exp) == 24 :
                        print(f"{exp} = 24")
                except ZeroDivisionError :
                    print(f"expression {exp} divides zero")

if __name__ == "__main__" :
    solve24(list(map(int, input().split())))