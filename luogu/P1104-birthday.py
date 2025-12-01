from typing import List
from functools import cmp_to_key

class Students :
    def __init__(
        self,
        name : str,
        year : int,
        month : int,
        day : int
    ) -> None :
        self.name  = name
        self.year  = year
        self.month = month
        self.day   = day

def sort_students(stu : List[Students]) -> None :
    def compare(a : Students, b : Students) -> int :
        if a.year < b.year :
            return -1
        elif a.year > b.year :
            return 1
        elif a.month < b.month :
            return -1
        elif a.month > b.month :
            return 1
        elif a.day < b.day :
            return -1
        elif a.day > b.day :
            return 1
        else :
            return 1

    stu.sort(key = cmp_to_key(compare))

if __name__ == "__main__" :
    n = int(input().rstrip())
    students : List[Students] = []

    for _ in range(n) :
        info = input().rstrip().split(" ")
        new_student = Students(info[0], int(info[1]), int(info[2]), int(info[3]))
        students.append(new_student)

    sort_students(students)

    for stu in students :
        print(stu.name)