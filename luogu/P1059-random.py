if __name__ == "__main__" :
    n = int(input().rstrip())

    numbers = list(map(int, input().rstrip().split(" ")))
    numbers = list(set(numbers))
    numbers.sort()

    print(len(numbers))
    print(" ".join(map(str, numbers)))