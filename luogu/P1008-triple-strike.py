from itertools import permutations

if __name__ == "__main__" :
    digits = range(1, 10)
    pt = permutations(digits)
    nums = ["".join(map(str, p)) for p in pt]

    for num in nums :
        num1 = int(num[0:3])
        num2 = int(num[3:6])
        num3 = int(num[6:])

        if num2 == num1 * 2 and num3 == num1 * 3 :
            print(f"{num1} {num2} {num3}")