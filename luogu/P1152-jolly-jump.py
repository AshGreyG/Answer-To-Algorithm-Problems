if __name__ == "__main__" :
    numbers = list(map(int, input().rstrip().split(" ")))
    n = numbers[0]
    numbers = numbers[1:]
    continues = list(range(1, n))

    for i in range(1, n) :
        if abs(numbers[i] - numbers[i - 1]) in continues :
            continues.remove(abs(numbers[i] - numbers[i - 1]))

    if len(continues) == 0 :
        print("Jolly")
    else :
        print("Not jolly")