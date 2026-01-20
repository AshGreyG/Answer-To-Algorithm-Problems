#include <iostream>
#include <vector>
#include <string>
#include <utility>

unsigned int calcMineNum(
    std::vector<std::vector<char>>& area,
    unsigned int x,
    unsigned int y
) {
    unsigned int sum = 0;
    std::vector<std::pair<unsigned int, unsigned int>> directions = {
        {1, 1},  {1, 0},  {1, -1},
        {-1, 1}, {-1, 0}, {-1, -1},
        {0, 1}, {0, -1}
    };
    for (const auto& dir : directions) {
        unsigned int newX = x + dir.first;
        unsigned int newY = y + dir.second;
        if (
            newX >= 1 && 
            newX <= area[0].size() - 1 && 
            newY >= 1 && 
            newY <= area.size() - 1
        ) {
            sum += area[newY][newX] == '*' ? 1 : 0;
        }
    }
    return sum;
}

int main() {
    unsigned int row, column;
    std::vector<std::vector<char>> mine_area;
    std::cin >> row >> column;
    mine_area.resize(row + 1, std::vector<char>(column + 1, '?'));
    for (int i = 1; i <= row; ++i) {
        std::string row_str;
        std::cin >> row_str;
        for (int j = 1; j <= column; ++j) {
            if (row_str[j - 1] == '*') {
                mine_area[i][j] = '*';
            }
        }
    }
    for (int i = 1; i <= row; ++i) {
        for (int j = 1; j <= column; ++j) {
            std::cout << (mine_area[i][j] == '*' ? "*" : std::to_string(calcMineNum(mine_area, j, i)));
        }
        std::cout << '\n';
    }
    return 0;
}