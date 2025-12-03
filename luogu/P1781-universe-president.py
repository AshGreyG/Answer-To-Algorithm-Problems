if __name__ == "__main__" :
    n = int(input().rstrip())
    maxstr = ""
    index = 0

    for i in range(n) :
        ballots = input().rstrip()

        if len(ballots) > len(maxstr) :
            maxstr = ballots
            index = i + 1
        elif len(ballots) == len(maxstr) and int(ballots) > int(maxstr) :
            maxstr = ballots
            index = i + 1

    print(index)
    print(maxstr)