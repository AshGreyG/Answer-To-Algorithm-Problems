from typing import List, Tuple

if __name__ == "__main__" :
    target_y, target_x, knight_y, knight_x = tuple(map(int, input().rstrip().split(" ")))
    board : List[List[int]] = []
    knight_moves : List[Tuple[int, int]] = [
        (knight_x + 2, knight_y + 1),
        (knight_x + 2, knight_y - 1),
        (knight_x - 2, knight_y + 1),
        (knight_x - 2, knight_y - 1),
        (knight_x + 1, knight_y + 2),
        (knight_x + 1, knight_y - 2),
        (knight_x - 1, knight_y + 2),
        (knight_x - 1, knight_y - 2),
        (knight_x,     knight_y)
    ]

    for _ in range(target_y + 1) :
        row : List[int] = [0] * (target_x + 1)
        board.append(row)

    board[0][0] = 1

    def check_move(x : int, y : int) -> int :
        if x < 0 or x >= target_x + 1 :
            return 0
        elif y < 0 or y >= target_y + 1 :
            return 0
        elif (x, y) in knight_moves :
            return 0
        else :
            return board[y][x]

    for i in range(target_y + 1) :
        for j in range(target_x + 1) :
            if not (i == 0 and j == 0) and not((j, i) in knight_moves) :
                board[i][j] = check_move(j, i - 1) + check_move(j - 1, i)

    print(board[target_y][target_x])