from typing import List
from functools import cmp_to_key

class StudentScore :
    def __init__(
        self,
        id : int,
        chinese : int,
        math : int, 
        english : int
    ) -> None :
        self.id = id
        self.chinese = chinese
        self.math = math
        self.english = english
        self.score = chinese + math + english

def student_compare(a : StudentScore, b : StudentScore) -> int :
    if a.score > b.score :
        return -1
    elif a.score < b.score :
        return 1
    elif a.chinese > b.chinese :
        return -1
    elif a.chinese < b.chinese :
        return 1
    elif a.id > b.id :
        return 1
    elif a.id < b.id :
        return -1
    else :
        return 0

if __name__ == "__main__" :
    n = int(input().rstrip())
    scores : List[StudentScore] = []

    for i in range(n) :
        score_str = input().rstrip().split(" ")
        score = StudentScore(
            i + 1,
            int(score_str[0]),
            int(score_str[1]),
            int(score_str[2]),
        )
        scores.append(score)

    scores.sort(key = cmp_to_key(student_compare))

    for i in range(min(len(scores), 5)) :
        sc = scores[i]
        print(f"{sc.id} {sc.score}")