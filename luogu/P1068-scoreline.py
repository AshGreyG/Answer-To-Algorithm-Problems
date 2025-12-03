from typing import List
from math import floor
from functools import cmp_to_key

class Applicant :
    def __init__(self, id : int, score : int) -> None :
        self.id = id
        self.score = score

def applicant_compare(a : Applicant, b : Applicant) -> int :
    if a.score > b.score :
        return -1
    elif a.score < b.score :
        return 1
    elif a.id > b.id :
        return 1
    elif a.id < b.id :
        return -1
    else :
        return 0

if __name__ == "__main__" :
    n, m = tuple(map(int, input().rstrip().split(" ")))
    applicants : List[Applicant] = []

    for _ in range(n) :
        id, score = tuple(map(int, input().rstrip().split(" ")))
        new = Applicant(id, score)
        applicants.append(new)

    applicants.sort(key = cmp_to_key(applicant_compare))
    last = min(floor(m * 1.5), n) - 1
    scoreline = applicants[last].score

    while True :
        if last <= n - 1 and applicants[last].score == scoreline :
            last += 1
        else :
            break

    print(f"{scoreline} {last}")

    for i in range(last) :
        print(f"{applicants[i].id} {applicants[i].score}")